import json
from io import StringIO


class RedisStream(StringIO):
    def __init__(self, confirmation, redis_client):
        """
        Create a new StringIO interface for the given key and redis_client.
        """
        StringIO.__init__(self)
        self.confirmation = confirmation
        self.redis_client = redis_client

    def write(self, record):
        """
        Publish record to redis logging list
        """
        if record != "\n":
            messages = self.redis_client.hget(self.confirmation, "messages")

            if messages:
                deserialized_messages = json.loads(messages)
                deserialized_messages.append(record)

                serialized_messages = json.dumps(
                    deserialized_messages,
                    separators=(",", ":")
                )

                self.redis_client.hset(
                    self.confirmation,
                    "messages",
                    serialized_messages
                )

            else:
                self.redis_client.hset(
                    self.confirmation,
                    "messages",
                    json.dumps([record])
                )
