import falcon

from resources.index import *
from resources.user import *
from resources.auth import *


class Router(object):

    def __init__(self, app):

        self.app = app

    def get_app(self):

        self.app.add_route('/', IndexController())

        self.app.add_route('/users', UserController())

        self.app.add_route('/login', LoginController())
        self.app.add_route('/activate/{code}', ActivateController())
        self.app.add_route('/logout', LogoutController())

        return self.app


        

