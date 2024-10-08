# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .event_destination_preferences_preferred import EventDestinationPreferencesPreferred
import typing
from .event_destination_preferences_enabled_item import EventDestinationPreferencesEnabledItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EventDestinationPreferences(UniversalBaseModel):
    preferred: EventDestinationPreferencesPreferred
    enabled: typing.List[EventDestinationPreferencesEnabledItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
