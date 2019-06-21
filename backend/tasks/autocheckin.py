import sys
from .celery import app
from utils import RedisCache
from utils import RedisStream
from southwest.checkin import auto_checkin


redis_client = RedisCache().connect()


@app.task(bind=True)
def autocheckin(self, confirmation, firstname, lastname, notifications=[]):
    redis_hash = {
        "task_id": self.id,
        "completed": "no"
    }

    try:
        redis_client.hmset(confirmation, redis_hash)

        sys.stdout = RedisStream(confirmation, redis_client)
        auto_checkin(confirmation, firstname, lastname, notifications)
    except (SystemExit, Exception) as exc:
        print(exc)
    finally:
        sys.stdout = sys.__stdout__
