import pykwalify.core


def _validate(data, schema):
    """
    Validates @data against the @schema.
    """
    pykwalify.core.Core(
        source_data=data,
        schema_data=schema
    ).validate(raise_exception=True)
