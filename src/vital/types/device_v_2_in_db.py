# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_facing_provider import ClientFacingProvider


class DeviceV2InDb(UniversalBaseModel):
    data: typing.Dict[str, typing.Optional[typing.Any]]
    provider_id: str
    user_id: str
    source_id: int
    id: str
    source: ClientFacingProvider

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
