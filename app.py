import os
from pyga import FlaskGATracker
from flask import Flask, request, session
from flask.ext.classy import FlaskView

from responder import Which

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


class AppView(FlaskView):
    route_base = '/'
    accepts = ["application/json", "application/xml", "application/javascript", "text/plain"]

    def _accepts(self, mime):
        best = request.accept_mimetypes.best_match([mime, 'text/html'])
        return best == mime and\
               request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

    def index(self):
        ga = FlaskGATracker('www.codingexcuses.com', 'UA-53020725-1')

        for method in self.accepts:
            if self._accepts(method):
                response, path = Which(method, request.args).get_response()
                ga.track(request, session, path=path)

                return response

        # Assume it's a browser
        response, path = Which("text/html", request.args).get_response()
        ga.track(request, session, path=path)
        return response

AppView.register(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
