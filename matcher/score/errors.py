from matcher.errors import Error


class InputRecordError(Error):
    """
    Non accepted empty input record Error.
    """
    message = 'Invalid Input Record found.'


class EmptyInputRecord(InputRecordError):
    """
    Non accepted empty input record Error.
    """
    details = 'The Input Record is empty.'


class MissingFieldInputRecord(Error):
    """
    Missing field on input record Error.
    """
    details = 'The Input Record is missing a field.'

    def __init__(self, missing_field=None):
        self.extra = 'Missing field: {}'.format(missing_field)


class WrongFormatFielddInputRecord(Error):
    """
    A field in the Input Record has a wrong format.
    """
    details = 'The Input Record has field with wrong format.'

    def __init__(self, field, valid_format, invalid_format):
        self.extra = '''Field: {} ({}) expected,
                        {} found'''.format(
                            field, valid_format, invalid_format
                        )
