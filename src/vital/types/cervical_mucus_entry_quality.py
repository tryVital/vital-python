# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CervicalMucusEntryQuality(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    DRY = "dry"
    STICKY = "sticky"
    CREAMY = "creamy"
    WATERY = "watery"
    EGG_WHITE = "egg_white"

    def visit(
        self,
        dry: typing.Callable[[], T_Result],
        sticky: typing.Callable[[], T_Result],
        creamy: typing.Callable[[], T_Result],
        watery: typing.Callable[[], T_Result],
        egg_white: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CervicalMucusEntryQuality.DRY:
            return dry()
        if self is CervicalMucusEntryQuality.STICKY:
            return sticky()
        if self is CervicalMucusEntryQuality.CREAMY:
            return creamy()
        if self is CervicalMucusEntryQuality.WATERY:
            return watery()
        if self is CervicalMucusEntryQuality.EGG_WHITE:
            return egg_white()
