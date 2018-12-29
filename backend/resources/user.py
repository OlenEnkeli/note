from libs.auth import auth_required, make_auth
from models.user import User
from schemas.user import UserPublicSchema


class UserController(object):

    def on_get(self, req, resp):

        users = self.session.query(User).all()

        resp.body = UserPublicSchema(many=True).dumps(users).data
