# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AllowedRadius(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    TEN = "10"
    TWENTY = "20"
    TWENTY_FIVE = "25"
    FIFTY = "50"

    def visit(
        self,
        ten: typing.Callable[[], T_Result],
        twenty: typing.Callable[[], T_Result],
        twenty_five: typing.Callable[[], T_Result],
        fifty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedRadius.TEN:
            return ten()
        if self is AllowedRadius.TWENTY:
            return twenty()
        if self is AllowedRadius.TWENTY_FIVE:
            return twenty_five()
        if self is AllowedRadius.FIFTY:
            return fifty()
