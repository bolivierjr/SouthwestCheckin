import re
import json
from api.extensions import ma
from marshmallow import fields, validate, ValidationError


def _validate_phone(data):
    if data:
        match = re.match(
            "^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})$",
            data,
        )

        if not match:
            raise ValidationError("Must enter in a valid phone number.")


class CheckinSchema(ma.Schema):
    confirmation = fields.String(required=True, validate=validate.Length(min=1))
    firstname = fields.String(required=True, validate=validate.Length(min=1))
    lastname = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(allow_none=True)
    phone = fields.String(allow_none=True, validate=_validate_phone)


class InfoSchema(ma.Schema):
    messages = fields.Method("_deserialize_and_remove_duplicates")
    running = fields.String()
    task_id = fields.String()
    confirmation = fields.String()

    def _deserialize_and_remove_duplicates(self, obj):
        data = obj["messages"]
        deserialized_data = json.loads(data)

        return list(dict.fromkeys(deserialized_data))
