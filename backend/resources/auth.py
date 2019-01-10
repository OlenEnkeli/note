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

        user_id = (
            session()
            .query(User.id)
            .filter(User.email == email)
            .filter(User.password ==
                hashlib.sha256(password.encode()).hexdigest())
            .filter(User.is_active == True)  # nopep8
            .one_or_none()
        )

        if not user_id:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        try:
            resp.set_cookie('user_session', make_session(email, user_id[0]))
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)


class LogoutController(object):

    @falcon.before(auth_required)
    def on_get(self, req, resp):

        if not self.current_user_id:
            raise falcon.HTTPError(falcon.HTTP_UNAUTHORIZED)

        remove_session(self.current_user.email)


class ActivateController(object):

    def on_get(self, req, resp, code):

        if not code:
            raise falcon.HTTPError(falcon.HTTP_BAD_REQUEST)

        user = (
            session()
            .query(User)
            .filter(User.activation_code == code)
            .one_or_none()
        )

        if not user:
            raise falcon.HTTPError(falcon.HTTP_NOT_FOUND)

        user.is_active = True
        user.activation_code = None

        session().commit()
