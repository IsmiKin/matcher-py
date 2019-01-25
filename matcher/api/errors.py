from matcher.errors import Error


class GenericAPIError(Error):
    """
    Generic API Error layout
    """
    status_code = 500


class WrongParamsAPIEndpointError(GenericAPIError):
    """
    Generic wrong params used on the API endpoint
    """
    message = 'Invalid params for the API Endpoint.'
    status_code = 422
