import os
import sys
from .celery import app
from southwest.checkin import auto_checkin
from redis import Redis
from utils import RedisStream

redis_creds = {
    "host": os.getenv("REDIS_HOST"),
    "port": int(os.getenv("REDIS_PORT"))
}

# Make a util for a single redis connection to distribute over the app
redis_client = Redis(**redis_creds)


@app.task(bind=True)
def autocheckin(self, confirmation, firstname, lastname, notifications=[]):
    sys.stdout = RedisStream(confirmation, redis_client)
    try:
        auto_checkin(confirmation, firstname, lastname, notifications)
    except (SystemExit, Exception) as exc:
        print(exc)
    finally:
        sys.stdout = sys.__stdout__
