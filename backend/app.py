import falcon

from libs.alchemy import alchemy_middleware

from routing import make_route

app = falcon.API(
    middleware=[
        alchemy_middleware()
    ]
)

app.resp_options.secure_cookies_by_default = False

make_route(app)
