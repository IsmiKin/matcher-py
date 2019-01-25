
from .validation import validate_process_file_endpoint
import matcher.utils as utils
import matcher.celery_app as celery_app


MIN_ACCEPTABLE_SCORE = 70

log = utils.get_logger()


def call_process_file_task(params):
    validate_process_file_endpoint(params)
    filename = params['filename']

    result = celery_app.process_file(filename)

    return result
