import os
import sys
from utils import RedisCache
from utils import RedisStream
from datetime import timedelta
from southwest.checkin import auto_checkin


redis_client = RedisCache().connect()


def autocheckin(confirmation, firstname, lastname, notifications):
    """
    Worker for multiprocessing Process.
    """
    _stdout = sys.stdout

    try:
        redis_client.hmset(confirmation, {"running": "True", "PID": os.getpid()})
        redis_client.expire(confirmation, timedelta(days=60))

        sys.stdout = RedisStream(confirmation, redis_client)
        auto_checkin(confirmation, firstname, lastname, notifications)

    except (SystemExit, Exception) as exc:
        print(exc)

    finally:
        sys.stdout = _stdout
        redis_client.hset(confirmation, "running", "False")
