# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingInsulinInjectionSampleType(str, enum.Enum):
    """
    Insulin type: rapid vs long acting ℹ️ This enum is non-exhaustive.
    """

    RAPID_ACTING = "rapid_acting"
    LONG_ACTING = "long_acting"
    _UNKNOWN = "__CLIENTFACINGINSULININJECTIONSAMPLETYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClientFacingInsulinInjectionSampleType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        rapid_acting: typing.Callable[[], T_Result],
        long_acting: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClientFacingInsulinInjectionSampleType.RAPID_ACTING:
            return rapid_acting()
        if self is ClientFacingInsulinInjectionSampleType.LONG_ACTING:
            return long_acting()
        return _unknown_member(self._value_)
