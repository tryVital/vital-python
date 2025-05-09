# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_facing_stand_duration_changed_event_type import ClientFacingStandDurationChangedEventType
from .grouped_stand_duration import GroupedStandDuration


class ClientFacingStandDurationChanged(UniversalBaseModel):
    event_type: ClientFacingStandDurationChangedEventType
    user_id: str
    client_user_id: str
    team_id: str
    data: GroupedStandDuration

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
