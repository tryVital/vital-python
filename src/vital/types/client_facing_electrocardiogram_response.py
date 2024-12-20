# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .client_facing_electrocardiogram import ClientFacingElectrocardiogram
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ClientFacingElectrocardiogramResponse(UniversalBaseModel):
    electrocardiogram: typing.List[ClientFacingElectrocardiogram]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
