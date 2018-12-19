from marshmallow_jsonapi import Schema, fields


class UserPublicSchema(Schema):

    id = fields.Integer()
    email = fields.String()
    name = fields.String()
    is_active = fields.Boolean()

    class Meta:
        type_ = "user"
