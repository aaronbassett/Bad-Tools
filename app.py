import random
import os

import yaml
from pyga import FlaskGATracker

from flask import Flask, jsonify, request, Response, render_template, session
from flask.ext.classy import FlaskView

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


class AppView(FlaskView):
    route_base = '/'

    def _accepts(self, mime):
        best = request.accept_mimetypes.best_match([mime, 'text/html'])
        return best == mime and\
               request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

    @property
    def _excuse(self):
        stream = open("excuses.yaml", 'r')
        excuses = yaml.load(stream)
        return random.choice(excuses["excuses"])

    def index(self):
        ga = FlaskGATracker('www.codingexcuses.com', 'UA-53020725-1')

        if self._accepts("application/json"):
            ga.track(request, session, path="/json/")
            return jsonify({
                "excuse": self._excuse
            })
        elif self._accepts("application/xml"):
            ga.track(request, session, path="/xml/")
            return Response(
                render_template('xml.xml', excuse=self._excuse),
                mimetype='text/xml'
            )
        elif self._accepts("application/javascript") or "jsonp" in request.args:
            ga.track(request, session, path="/jsonp/")
            return Response(
                render_template('jsonp.js', excuse=self._excuse),
                mimetype='application/javascript'
            )
        elif self._accepts("text/plain"):
            ga.track(request, session, path="/text/")
            return Response("Hello world", mimetype='text/plain')
        else:
            return render_template('html.html', excuse=self._excuse)

AppView.register(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
