import falcon
import bcrypt

from config import config
from models.user import User

from libs.alchemy import alchemy_session

session_storage = {}


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    if req.cookies['user_session'] not in session_storage:
        raise falcon.HTTPUnauthorized()

    resource.current_user = session_storage[req.cookies['user_session']]


def make_auth(email):

    if email in session_storage.values():
        return False

    user_credential = email+config['secure']['salt_session']

    session = str(
        bcrypt
        .hashpw(user_credential.encode(), bcrypt.gensalt()),
        'utf-8'
    )

    current_user = (
        alchemy_session()
        .query(User)
        .filter(User.email == email)
        .one()
    )

    session_storage[session] = current_user

    return session
