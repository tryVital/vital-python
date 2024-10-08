# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .period import Period
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RelativeTimeframe(UniversalBaseModel):
    type: typing.Literal["relative"] = "relative"
    anchor: str
    past: Period

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
