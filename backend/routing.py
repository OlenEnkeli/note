import falcon

from resources.index import *
from resources.user import *
from resources.auth import *


def make_route(app):
    
    app.add_route('/', IndexController())

    app.add_route('/users', UserController())

    app.add_route('/login', LoginController())
    app.add_route('/activate/{code}', ActivateController())
    app.add_route('/logout', LogoutController())

