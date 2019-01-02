import falcon
import hashlib

from marshmallow import Schema, fields

from config import config
from libs.alchemy import session
from libs.auth import auth_required, make_session, remove_session
from libs.decorators import with_body_params
from models.user import User


class LoginController(object):

    @with_body_params(
        email=fields.String(required=True),
        password=fields.String(required=True)
    )
    def on_post(self, req, resp):

        email = req.parsed['email']
        password = req.parsed['password']+config['secure']['salt_password']

        user = (
            session()
            .query(User)
            .filter(User.email == email)
            .filter(User.password == hashlib.sha256(password.encode()).hexdigest())
            .one_or_none()
        )

        if not user:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        try:
            resp.set_cookie('user_session', make_session(email, user))
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)


class LogoutController(object):

    @falcon.before(auth_required)
    def on_get(self, req, resp):
        
        if not self.current_user:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        remove_session(self.current_user.email)
        

        

