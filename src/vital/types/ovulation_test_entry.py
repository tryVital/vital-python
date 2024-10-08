# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .ovulation_test_entry_test_result import OvulationTestEntryTestResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class OvulationTestEntry(UniversalBaseModel):
    date: str
    test_result: OvulationTestEntryTestResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
