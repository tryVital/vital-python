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

    def visit(
        self, rapid_acting: typing.Callable[[], T_Result], long_acting: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ClientFacingInsulinInjectionSampleType.RAPID_ACTING:
            return rapid_acting()
        if self is ClientFacingInsulinInjectionSampleType.LONG_ACTING:
            return long_acting()
