from typing import Any


class BaseError(Exception):
    def __init__(
        self,
        message,
        type,
        code,
    ):
        super(BaseError, self).__init__(message)

        # In Python 3, the Exception class does not expose a `message`
        # attribute so we need to set it explicitly. See
        # https://www.python.org/dev/peps/pep-0352/#retracted-ideas.
        self.message = message

        self.type = type
        self.code = code


class VitalError(BaseError):
    def __init__(
        self,
        message,
        type,
        code,
        causes=None,
    ):
        super(VitalError, self).__init__(
            message,
            type,
            code,
        )
        self.causes = [
            VitalCause(
                cause["error_message"],
                cause["error_type"],
                cause["error_code"],
            )
            for cause in causes or []
        ]

    @staticmethod
    def from_response(response: Any, status_code: int) -> "VitalError":
        """
        Create an error of the right class from an API response.
        :param   response    dict        Response JSON
        """
        if type(response) == str:
            return InvalidRequestError(
                f"{status_code} - {response}", "INVALID_REQUEST", status_code
            )
        if not type(response) == dict:
            raise InvalidRequestError("Invalid request", "INVALID_REQUEST", 400)
        if response.get("message"):
            return InvalidRequestError(
                response.get("message"), "INVALID_REQUEST", status_code
            )
        if not response.get("error_type"):
            return InvalidRequestError("Invalid request", "INVALID_REQUEST", 400)
        cls = VITAL_ERROR_TYPE_MAP.get(response["error_type"], VitalError)
        return cls(
            response["error_message"],
            response["error_type"],
            status_code,
            response.get("causes"),
        )


class VitalCause(BaseError):
    def __init__(
        self,
        message,
        type,
        code,
    ):
        super(VitalCause, self).__init__(
            message,
            type,
            code,
        )


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


class SignatureVerificationError(VitalError):
    def __init__(self, message: str, sig_header: str):
        super(SignatureVerificationError, self).__init__(
            message, "INVALID_REQUEST", None
        )
        self.sig_header = sig_header


VITAL_ERROR_TYPE_MAP = {
    "INVALID_REQUEST": InvalidRequestError,
    "INVALID_INPUT": InvalidInputError,
    "RATE_LIMIT_EXCEEDED": RateLimitExceededError,
    "API_ERROR": APIError,
}
