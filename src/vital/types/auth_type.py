# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthType(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    PASSWORD = "password"
    OAUTH = "oauth"
    EMAIL = "email"
    _UNKNOWN = "__AUTHTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "AuthType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        password: typing.Callable[[], T_Result],
        oauth: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is AuthType.PASSWORD:
            return password()
        if self is AuthType.OAUTH:
            return oauth()
        if self is AuthType.EMAIL:
            return email()
        return _unknown_member(self._value_)
