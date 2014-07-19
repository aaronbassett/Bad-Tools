import random

import yaml

from flask import Flask, jsonify, request, Response, render_template
from flask.ext.classy import FlaskView

app = Flask(__name__)
app.debug = True


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

        if self._accepts("application/json"):
            return jsonify({
                "excuse": self._excuse
            })
        elif self._accepts("application/xml"):
            return Response(
                render_template('xml.xml', excuse=self._excuse),
                mimetype='text/xml'
            )
        elif self._accepts("application/javascript") or "jsonp" in request.args:
            return Response(
                render_template('jsonp.js', excuse=self._excuse),
                mimetype='application/javascript'
            )
        elif self._accepts("text/plain"):
            return Response("Hello world", mimetype='text/plain')
        else:
            return render_template('html.html', excuse=self._excuse)

AppView.register(app)

if __name__ == '__main__':
    app.run()
