import json
import falcon

from libs.auth import auth_required


class IndexController(object):

    @falcon.before(auth_required)
    def on_get(self, req, resp):
        print(self.current_user)
        resp.body = json.dumps({'version': '0.0.1'})
        
