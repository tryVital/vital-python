# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .sleep_cycle import SleepCycle
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ClientSleepCycleResponse(UniversalBaseModel):
    sleep_cycle: typing.List[SleepCycle]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow