import yaml
import pykwalify.core
from pykwalify import errors as pykwalify_errors
from .errors import WrongParamsAPIEndpointError


PROCESS_FILE_TEMPLATE = """---
type: map
allowempty: false
mapping:
  filename:
    type: str
    required: true
    pattern: '(\\\\?([^\\/]*[\\/])*)([^\\/]+)$'
"""


def validate_process_file_endpoint(params):
    validation_schema = yaml.load(PROCESS_FILE_TEMPLATE)

    try:
        _validate(params, validation_schema)
    except pykwalify_errors.PyKwalifyException as e:
        msg = (
            'Params failed validation. '
            'Exception: ({0}).'.format(e)
        )

        extra = e.msg.split('\n - ')[1:] if '\n' in e.msg else e.msg

        raise WrongParamsAPIEndpointError(msg, extra)


def _validate(data, schema):
    """
    Validates @data against the @schema.
    """
    pykwalify.core.Core(
        source_data=data,
        schema_data=schema
    ).validate(raise_exception=True)
