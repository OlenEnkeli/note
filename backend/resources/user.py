import falcon
import hashlib

from marshmallow import Schema, fields

from config import config
from libs.alchemy import session
from libs.decorators import with_body_params
from libs.auth import auth_required
from models.user import User
from schemas.user import UserSchema


class UserController(object):

    @falcon.before(auth_required)
    def on_get(self, req, resp):
        resp.body = UserSchema().dumps(self.current_user).data

    @with_body_params(
        email=fields.String(required=True),
        password=fields.String(required=True),
        name=fields.String(required=True)
    )
    def on_post(self, req, resp):

        user = User(**req.parsed)

        password = user.password+config['secure']['salt_password']
        activation_code = user.email+config['secure']['salt_activation']

        user.password = hashlib.sha256(password.encode()).hexdigest()
        user.activation_code = hashlib.sha256(activation_code.encode())\
            .hexdigest()

        session().add(user)

        try:
            session().commit()
        except Exception:
            raise(falcon.HTTPError(falcon.HTTP_UNPROCESSABLE_ENTITY))
