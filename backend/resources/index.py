import json

from libs.email import send_mail


class IndexController(object):

    def on_get(self, req, resp):

        resp.body = json.dumps({'version': '0.0.1'})
