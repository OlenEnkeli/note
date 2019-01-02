import falcon
import hashlib

from config import config
from models.user import User

session_storage = {}


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    if req.cookies['user_session'] not in session_storage:
        raise falcon.HTTPUnauthorized()

    resource.current_user = session_storage[req.cookies['user_session']]


def make_session(credential, user_object):

    user_credential = credential+config['secure']['salt_session']

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    if session in session_storage:
        return False

    session_storage[session] = user_object

    print(session_storage)

    return session


def remove_session(credential):

    user_credential = credential+config['secure']['salt_session']

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    if session not in session_storage:
        return False
    
    session_storage.pop(session)

