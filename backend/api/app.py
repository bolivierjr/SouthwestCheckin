import os
import signal
from utils import RedisCache
from tasks import autocheckin
from api.extensions import ma
from multiprocessing import Process
from marshmallow import ValidationError
from flask import Flask, request, jsonify
from redis.exceptions import ConnectionError
from api.schemas import CheckinSchema, InfoSchema


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] == os.getenv("SECRET_KEY")

    # Initialize flask-marshmallow extension
    ma.init_app(app)

    redis_client = RedisCache().connect()

    @app.route("/checkin", methods=["POST"])
    def checkin():
        try:
            CheckinSerializer = CheckinSchema()
            checkin_data = CheckinSerializer.loads(request.data)

            confirmation = checkin_data.get("confirmation")
            firstname = checkin_data.get("firstname")
            lastname = checkin_data.get("lastname")
            email = checkin_data.get("email")
            phone = checkin_data.get("phone")

            flight_confirm = redis_client.exists(confirmation)
            running_task = redis_client.hget(confirmation, "running")

            if flight_confirm and running_task == "True":
                return (
                    jsonify(
                        {"error": "A task is already running for this confirmation."}
                    ),
                    400,
                )

            # Delete any existing messages if any
            redis_client.hdel(confirmation, "messages")

            # Check if there are any optional email or phone fields
            # sent to get a notification back on checkin.
            notifications = []
            if email is not None:
                notifications.append({"mediaType": "EMAIL", "emailAddress": email})
            if phone is not None:
                notifications.append({"mediaType": "SMS", "phoneNumber": phone})

            # Run the auto_checkin script in a background task with multiprocessing.
            proc = Process(
                target=autocheckin,
                args=(confirmation, firstname, lastname, notifications),
            )
            proc.start()

            return (
                jsonify({"status": "Created a new SouthwestCheckin task successfully"}),
                200,
            )

        except ValidationError as exc:
            return jsonify({"error": exc.messages}), 422

        except (ConnectionError, TypeError, Exception):
            return jsonify({"error": "There was an error. Contact admin at once."}), 500

    @app.route("/info/<string:confirmation>", methods=["GET", "DELETE"])
    def info(confirmation):
        try:
            checkin_info = redis_client.hgetall(confirmation)

            if not checkin_info:
                return (
                    jsonify({"status": "No tasks running with this confirmation."}),
                    200,
                )

            elif request.method == "DELETE":
                pid = checkin_info.get("PID")
                running = checkin_info.get("running")

                # Kill process if running
                if pid and running == "True":
                    os.kill(int(pid), signal.SIGTERM)

                # Delete the confirmation info from redis
                redis_client.delete(confirmation)

                return jsonify({"status": "Task deleted successfully."}), 200

            InfoSerializer = InfoSchema()

            return InfoSerializer.jsonify(checkin_info), 200

        except (ConnectionError, Exception):
            return (
                jsonify({"status": "There was an error. Contact admin at once."}),
                500,
            )

    return app
