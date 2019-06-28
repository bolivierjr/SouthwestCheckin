import json
from api.extensions import ma
from marshmallow import fields, validate


class CheckinSchema(ma.Schema):
    confirmation = fields.String(required=True, validate=validate.Length(1))
    firstname = fields.String(required=True, validate=validate.Length(1))
    lastname = fields.String(required=True, validate=validate.Length(1))


class InfoSchema(ma.Schema):
    messages = fields.Method("_deserialize_and_remove_duplicates")
    running = fields.String()
    task_id = fields.String()
    confirmation = fields.String()

    def _deserialize_and_remove_duplicates(self, obj):
        data = obj["messages"]
        deserialized_data = json.loads(data)
        
        return list(dict.fromkeys(deserialized_data))
