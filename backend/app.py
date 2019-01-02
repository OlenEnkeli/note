import falcon
import bjoern

from libs.alchemy import alchemy_middleware

from routing import Router


app = falcon.API(
    middleware=[
        alchemy_middleware()
    ]
)

app.resp_options.secure_cookies_by_default = False

app = Router(app).get_app()
