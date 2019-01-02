import falcon
import bcrypt

from config import config
from models.user import User

session_storage = {}


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    if req.cookies['user_session'] not in session_storage:
        raise falcon.HTTPUnauthorized()

    resource.current_user = session_storage[req.cookies['user_session']]


def make_auth(credential, user_object):

    if credential in session_storage:
        return False

    user_credential = credential+config['secure']['salt_session']

    session = str(
        bcrypt
        .hashpw(user_credential.encode(), bcrypt.gensalt()),
        'utf-8'
    )

    session_storage[session] = user_object

    print(session_storage)

    return session
