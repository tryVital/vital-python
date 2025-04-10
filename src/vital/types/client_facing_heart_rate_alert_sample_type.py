# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClientFacingHeartRateAlertSampleType(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    LOW_HEART_RATE = "low_heart_rate"
    HIGH_HEART_RATE = "high_heart_rate"
    IRREGULAR_RHYTHM = "irregular_rhythm"

    def visit(
        self,
        low_heart_rate: typing.Callable[[], T_Result],
        high_heart_rate: typing.Callable[[], T_Result],
        irregular_rhythm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientFacingHeartRateAlertSampleType.LOW_HEART_RATE:
            return low_heart_rate()
        if self is ClientFacingHeartRateAlertSampleType.HIGH_HEART_RATE:
            return high_heart_rate()
        if self is ClientFacingHeartRateAlertSampleType.IRREGULAR_RHYTHM:
            return irregular_rhythm()
