from flask import jsonify, Response, render_template
from utils import get_excuse


class Which(object):

    def __init__(self, mime_type, args):
        self.mime_type = mime_type
        self.args = args

    @property
    def _excuse(self):
        return get_excuse()

    def get_response(self):
        if self.mime_type == "application/json":
            return jsonify({
                "excuse": self._excuse
            }), "/json/"

        elif self.mime_type == "application/xml":
            return Response(
                render_template('xml.xml', excuse=self._excuse),
                mimetype='text/xml'
            ), "/xml/"

        elif self.mime_type == "application/javascript" or "jsonp" in self.args:
            return Response(
                render_template('jsonp.js', excuse=self._excuse),
                mimetype='application/javascript'
            ), "/jsonp/"

        elif self.mime_type == "text/plain":
            return Response(self._excuse, mimetype='text/plain'), "/text/"

        else:
            return render_template('html.html', excuse=self._excuse), "/html/"
