

class Error(Exception):
    """
    Base class for all errors.
    """
    message = 'An unknown error occured.'

    def __init__(self, details, extra=None):
        self.details = details
        self.extra = extra

    def __str__(self):
        return self.message

    def __repr__(self):
        return '{0} Details: {1}'.format(
            self.message,
            self.details
        )
