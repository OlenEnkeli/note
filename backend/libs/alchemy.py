from config import config

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    '{engine}://{user}:{password}@{host}:{port}/{db}'.format(**config['db'])
)

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)


class SQLAlchemySessionManager:

    def __init__(self, session):
        self.session = session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            session.remove()


def alchemy_middleware():
    return SQLAlchemySessionManager(session)


def alchemy_session():
    return session
