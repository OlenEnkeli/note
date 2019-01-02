from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Integer()
    email = fields.String()
    name = fields.String()
    is_active = fields.Boolean()

    class Meta:
        type_ = "user"
