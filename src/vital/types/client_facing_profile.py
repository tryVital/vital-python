# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_facing_source import ClientFacingSource
from .gender import Gender
from .sex import Sex


class ClientFacingProfile(UniversalBaseModel):
    id: str
    user_id: str = pydantic.Field()
    """
    User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api.
    """

    height: typing.Optional[int] = None
    birth_date: typing.Optional[str] = None
    wheelchair_use: typing.Optional[bool] = None
    gender: typing.Optional[Gender] = None
    sex: typing.Optional[Sex] = None
    source: ClientFacingSource
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
