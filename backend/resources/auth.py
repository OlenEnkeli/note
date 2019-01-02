import falcon
import bcrypt

from marshmallow import Schema, fields

from config import config
from libs.alchemy import session
from libs.auth import auth_required, make_auth
from libs.decorators import with_body_params
from models.user import User


class LoginController(object):

    def __init__(self):
        self.user_storage = {}

    @with_body_params(
        email=fields.String(required=True),
        password=fields.String(required=True)
    )
    def on_post(self, req, resp):

        email = req.parsed['email']
        password = req.parsed['password']

        user = session().query(User).filter(User.email == email).one_or_none()

        if not user:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        try:
            if not bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
                raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        resp.set_cookie('user_session', make_auth(email, user))
