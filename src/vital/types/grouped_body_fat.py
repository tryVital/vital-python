# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_facing_body_fat_timeseries import ClientFacingBodyFatTimeseries
from .client_facing_source import ClientFacingSource


class GroupedBodyFat(UniversalBaseModel):
    source: ClientFacingSource
    data: typing.List[ClientFacingBodyFatTimeseries]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
