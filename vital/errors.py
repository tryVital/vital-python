class BaseError(Exception):
    def __init__(
        self,
        message,
        type,
        code,
        display_message,
    ):
        super(BaseError, self).__init__(message)

        # In Python 3, the Exception class does not expose a `message`
        # attribute so we need to set it explicitly. See
        # https://www.python.org/dev/peps/pep-0352/#retracted-ideas.
        self.message = message

        self.type = type
        self.code = code
        self.display_message = display_message


class VitalError(BaseError):
    def __init__(
        self,
        message,
        type,
        code,
        display_message,
        request_id="",
        causes=None,
    ):
        super(VitalError, self).__init__(
            message,
            type,
            code,
            display_message,
        )
        self.request_id = request_id
        self.causes = [
            VitalCause(
                cause["error_message"],
                cause["error_type"],
                cause["error_code"],
                cause.get("display_message", ""),
                cause["item_id"],
            )
            for cause in causes or []
        ]

    @staticmethod
    def from_response(response):
        """
        Create an error of the right class from an API response.
        :param   response    dict        Response JSON
        """
        cls = VITAL_ERROR_TYPE_MAP.get(response["error_type"], VitalError)
        return cls(
            response["error_message"],
            response["error_type"],
            response["error_code"],
            response["display_message"],
            response["request_id"],
            response.get("causes"),
        )


class VitalCause(BaseError):
    def __init__(
        self,
        message,
        type,
        code,
        display_message,
        item_id,
    ):
        super(VitalCause, self).__init__(
            message,
            type,
            code,
            display_message,
        )
        self.item_id = item_id


class InvalidRequestError(VitalError):
    """The request is malformed and cannot be processed."""

    pass


class InvalidInputError(VitalError):
    """The request is correctly formatted, but the values are incorrect."""

    pass


class RateLimitExceededError(VitalError):
    """The request is valid but has exceeded established rate limits."""

    pass


class APIError(VitalError):
    """Planned maintenance or an API internal server error."""

    pass


VITAL_ERROR_TYPE_MAP = {
    "INVALID_REQUEST": InvalidRequestError,
    "INVALID_INPUT": InvalidInputError,
    "RATE_LIMIT_EXCEEDED": RateLimitExceededError,
    "API_ERROR": APIError,
}
