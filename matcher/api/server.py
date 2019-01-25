"""
Feed Management API wrapper for gunicorn.
"""

from flask import request
from flask import Flask
import simplejson
import logging

from matcher.api.views import process_file

stream_handler = logging.StreamHandler()
log_format = logging.Formatter(
    fmt='%(asctime)s %(name)s.%(levelname)s: %(message)s'
)


def create_app():
    """
    Application factory.
    """
    app = Flask(__name__)

    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(process_file)

    @app.errorhandler(404)
    def page_not_found(e):
        return generate_response(
            [],
            return_code=str(404),
            reason='Page not found.'
        )

    @app.errorhandler(500)
    def internal_server_error(e):
        return generate_response(
            [],
            return_code=str(500),
            reason='Internal server error.'
        )

    return app


app = create_app()


@app.before_request
def before():
    app.logger.info(
        "Request: {method} {path}".format(
            method=request.method, path=request.path
        )
    )
    app.logger.info(
        "Request body: {}".format(request.get_json())
    )


def generate_response(payload, return_code=200, reason=None):
    rtn = {
        'status': str(return_code),
        'reason': reason,
        'payload': payload
    }
    return (
        simplejson.dumps(rtn),
        return_code,
        {'Content-Type': 'application/json'}
    )
