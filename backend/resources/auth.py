from marshmallow_jsonapi import Schema, fields

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

        resp.set_cookie('user_session', make_auth(email))
