# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_facing_food import ClientFacingFood
from .client_facing_source import ClientFacingSource
from .energy import Energy
from .macros import Macros
from .micros import Micros


class MealInDbBaseClientFacingSource(UniversalBaseModel):
    id: str
    user_id: str
    priority_id: int = pydantic.Field()
    """
    This value has no meaning.
    """

    source_id: int = pydantic.Field()
    """
    This value has no meaning.
    """

    provider_id: str = pydantic.Field()
    """
    This value is identical to `id`.
    """

    timestamp: dt.datetime
    name: str
    energy: typing.Optional[Energy] = None
    macros: typing.Optional[Macros] = None
    micros: typing.Optional[Micros] = None
    data: typing.Optional[typing.Dict[str, ClientFacingFood]] = None
    source: ClientFacingSource
    created_at: dt.datetime
    updated_at: dt.datetime
    source_app_id: typing.Optional[str] = None
    source_device_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
