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

