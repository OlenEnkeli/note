import falcon
import hashlib

from config import config
from models.user import User
from libs.alchemy import session
from libs.redis import Redis

def auth_required(req,resp,resource, params):
    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user_id = Redis.get(req.cookies['user_session'])

    if not user_id:
        raise falcon.HTTPUnauthorized()
    
    resource.current_user_id = int(user_id)


def user_required(req,resp,resource, params):
    auth_required(req,resp,resource,params)

    if resource.current_user_id:
        resource.current_user = (
                session()
                .query(User)
                .filter(User.id == resource.current_user_id)
                .one()
        )


def make_session(credential, user_id):

    user_credential = credential+config['secure']['salt_session']

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    if Redis.get(session):
        return False

    Redis.set(session, user_id)

    return session


def remove_session(credential):

    user_credential = credential+config['secure']['salt_session']

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    if not Redis.get(session):
        return False
    
    Redis.delete(session)

    
