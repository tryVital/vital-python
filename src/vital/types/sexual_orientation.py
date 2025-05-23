# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SexualOrientation(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    LESBIAN_GAY_OR_HOMOSEXUAL = "lesbian_gay_or_homosexual"
    HETEROSEXUAL_OR_STRAIGHT = "heterosexual_or_straight"
    BISEXUAL = "bisexual"
    DONT_KNOW = "dont_know"
    OTHER = "other"
    _UNKNOWN = "__SEXUALORIENTATION_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "SexualOrientation":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        lesbian_gay_or_homosexual: typing.Callable[[], T_Result],
        heterosexual_or_straight: typing.Callable[[], T_Result],
        bisexual: typing.Callable[[], T_Result],
        dont_know: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is SexualOrientation.LESBIAN_GAY_OR_HOMOSEXUAL:
            return lesbian_gay_or_homosexual()
        if self is SexualOrientation.HETEROSEXUAL_OR_STRAIGHT:
            return heterosexual_or_straight()
        if self is SexualOrientation.BISEXUAL:
            return bisexual()
        if self is SexualOrientation.DONT_KNOW:
            return dont_know()
        if self is SexualOrientation.OTHER:
            return other()
        return _unknown_member(self._value_)
