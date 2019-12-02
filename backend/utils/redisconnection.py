import os
import threading
from redis import Redis


REDIS_CREDS = {"host": os.getenv("REDIS_HOST"), "port": int(os.getenv("REDIS_PORT"))}


class RedisCache:
    """
    Creates a singleton to make a global redis connection
    that is thread-safe to use throughout the app
    """
    _lock = threading.Lock()

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            with cls._lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(RedisCache, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self._redis_connection = Redis(**REDIS_CREDS, decode_responses=True)

    def connect(self):
        return self._redis_connection
