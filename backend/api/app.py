import os
import json
from utils import RedisCache
from tasks import autocheckin
from api.extensions import ma
from marshmallow import ValidationError
from flask import Flask, request, jsonify
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
            CheckinSerializer = CheckinSchema(strict=True)
            checkin_data = CheckinSerializer.loads(request.data).data

            confirmation = checkin_data.get("confirmation")
            firstname = checkin_data.get("firstname")
            lastname = checkin_data.get("lastname")

            flight_confirm = redis_client.exists(confirmation)
            running_task = redis_client.hget(confirmation, "running")

            if flight_confirm and running_task == "True":
                return jsonify(
                    {"error": "Task already running for this confirmation number."}
                ), 400

            # Delete any existing messages if any
            redis_client.hdel(confirmation, "messages")
            # Run the auto_checkin script celery task in the background
            autocheckin.delay(confirmation, firstname, lastname)

        except ValidationError as exc:
            return jsonify({"error": exc.messages}), 422

        except (TypeError, Exception) as exc:
            return jsonify({"error": exc}), 500

        return jsonify(
            {"status": "Created a new SouthwestCheckin task successfully"}
        ), 200

    @app.route("/info/<string:confirmation>", methods=["GET"])
    def info(confirmation):
        try:
            checkin_info = redis_client.hgetall(confirmation)

            if not checkin_info:
                return jsonify(
                    {"status": "No tasks running with this confirmation."}
                ), 200

            InfoSerializer = InfoSchema(strict=True)

            return InfoSerializer.jsonify(checkin_info), 200

        except Exception as exc:
            return jsonify({"error": exc}), 500

    return app
