# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HistoricalPullStatus(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    SUCCESS = "success"
    FAILURE = "failure"
    IN_PROGRESS = "in_progress"
    SCHEDULED = "scheduled"
    RETRYING = "retrying"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        retrying: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HistoricalPullStatus.SUCCESS:
            return success()
        if self is HistoricalPullStatus.FAILURE:
            return failure()
        if self is HistoricalPullStatus.IN_PROGRESS:
            return in_progress()
        if self is HistoricalPullStatus.SCHEDULED:
            return scheduled()
        if self is HistoricalPullStatus.RETRYING:
            return retrying()
