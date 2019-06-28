import sys
from .celery import app
from utils import RedisCache
from utils import RedisStream
from datetime import timedelta
from southwest.checkin import auto_checkin


redis_client = RedisCache().connect()


@app.task(bind=True)
def autocheckin(self, confirmation, firstname, lastname, notifications=[]):
    try:
        redis_client.hset(confirmation, "running", "True")
        redis_client.expire(confirmation, timedelta(days=60))

        sys.stdout = RedisStream(confirmation, redis_client)
        auto_checkin(confirmation, firstname, lastname, notifications)
    except (SystemExit, Exception) as exc:
        print(exc)

    redis_client.hset(confirmation, "running", "False")
