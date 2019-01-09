import json
import falcon

from libs.auth import auth_required


class IndexController(object):

    def on_get(self, req, resp):

        resp.body = json.dumps({'version': '0.0.1'})
