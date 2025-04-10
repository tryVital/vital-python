# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Labs(str, enum.Enum):
    """
    ℹ️ This enum is non-exhaustive.
    """

    AYUMETRIX = "ayumetrix"
    SPIRIPLEX = "spiriplex"
    USSL = "ussl"
    QUEST = "quest"
    LABCORP = "labcorp"
    BIOREFERENCE = "bioreference"
    US_BIOTEK = "us_biotek"
    MANUAL = "manual"
    SANOCARDIO = "sanocardio"
    IHD = "ihd"

    def visit(
        self,
        ayumetrix: typing.Callable[[], T_Result],
        spiriplex: typing.Callable[[], T_Result],
        ussl: typing.Callable[[], T_Result],
        quest: typing.Callable[[], T_Result],
        labcorp: typing.Callable[[], T_Result],
        bioreference: typing.Callable[[], T_Result],
        us_biotek: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        sanocardio: typing.Callable[[], T_Result],
        ihd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Labs.AYUMETRIX:
            return ayumetrix()
        if self is Labs.SPIRIPLEX:
            return spiriplex()
        if self is Labs.USSL:
            return ussl()
        if self is Labs.QUEST:
            return quest()
        if self is Labs.LABCORP:
            return labcorp()
        if self is Labs.BIOREFERENCE:
            return bioreference()
        if self is Labs.US_BIOTEK:
            return us_biotek()
        if self is Labs.MANUAL:
            return manual()
        if self is Labs.SANOCARDIO:
            return sanocardio()
        if self is Labs.IHD:
            return ihd()
