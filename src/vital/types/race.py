# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Race(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    AFRICAN_AMERICAN_OR_BLACK = "african_american_or_black"
    ASIAN = "asian"
    INDIGENOUS_NATIVE_AMERICAN_ALASKA_NATIVE = "indigenous_native_american_alaska_native"
    OTHER = "other"
    PACIFIC_ISLANDER_OR_HAWAIIAN = "pacific_islander_or_hawaiian"
    WHITE_CAUCASIAN = "white_caucasian"

    def visit(
        self,
        african_american_or_black: typing.Callable[[], T_Result],
        asian: typing.Callable[[], T_Result],
        indigenous_native_american_alaska_native: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        pacific_islander_or_hawaiian: typing.Callable[[], T_Result],
        white_caucasian: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Race.AFRICAN_AMERICAN_OR_BLACK:
            return african_american_or_black()
        if self is Race.ASIAN:
            return asian()
        if self is Race.INDIGENOUS_NATIVE_AMERICAN_ALASKA_NATIVE:
            return indigenous_native_american_alaska_native()
        if self is Race.OTHER:
            return other()
        if self is Race.PACIFIC_ISLANDER_OR_HAWAIIAN:
            return pacific_islander_or_hawaiian()
        if self is Race.WHITE_CAUCASIAN:
            return white_caucasian()
