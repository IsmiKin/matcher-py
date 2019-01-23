from flask import current_app
import traceback
import simplejson

import matcher.errors as errors


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


def handle_errors(func):
    """
    Decorator handling errors in requests.
    """
    def wrapped_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except errors.Error as e:
            current_app.logger.warning(
                'Handled error: ({0}).'.format(repr(e))
            )

            payload = []
            if e.extra:
                payload = e.extra
            return generate_response(
                payload,
                return_code=str(e.status_code),
                reason=str(e)
            )

        except Exception as e:
            current_app.logger.error(
                'Unhandled exception: ({0}). Traceback: ({1}).'.format(
                    repr(e),
                    traceback.format_exc()
                )
            )

            return generate_response(
                [],
                return_code=str(500),
                reason='An unknown error occured.'
            )

    wrapped_func.__name__ = func.__name__
    return wrapped_func
