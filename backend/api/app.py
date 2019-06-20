import os
from flask import Flask, jsonify
from tasks import autocheckin


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] == os.getenv("SECRET_KEY")

    @app.route("/api/checkin")
    def index():
        # Using fake parameters for testing right now. Make
        # this accept real parameters from endpoint and clean
        try:
            autocheckin.delay("xxxxxx", "bruce", "olivier")
        except (TypeError, Exception) as exc:
            return jsonify({"error": f"{exc}"})

        return jsonify({"status": "ok"})

    return app
