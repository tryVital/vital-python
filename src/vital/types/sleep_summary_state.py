# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SleepSummaryState(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    TENTATIVE = "tentative"
    CONFIRMED = "confirmed"

    def visit(self, tentative: typing.Callable[[], T_Result], confirmed: typing.Callable[[], T_Result]) -> T_Result:
        if self is SleepSummaryState.TENTATIVE:
            return tentative()
        if self is SleepSummaryState.CONFIRMED:
            return confirmed()
