# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PayorCodeExternalProvider(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    CHANGE_HEALTHCARE = "change_healthcare"
    AVAILITY = "availity"
    STEDI = "stedi"
    _UNKNOWN = "__PAYORCODEEXTERNALPROVIDER_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "PayorCodeExternalProvider":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        change_healthcare: typing.Callable[[], T_Result],
        availity: typing.Callable[[], T_Result],
        stedi: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is PayorCodeExternalProvider.CHANGE_HEALTHCARE:
            return change_healthcare()
        if self is PayorCodeExternalProvider.AVAILITY:
            return availity()
        if self is PayorCodeExternalProvider.STEDI:
            return stedi()
        return _unknown_member(self._value_)
