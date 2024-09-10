# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .query_config_week_starts_on import QueryConfigWeekStartsOn
from .query_config_provider_priority_overrides_item import QueryConfigProviderPriorityOverridesItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class QueryConfig(UniversalBaseModel):
    week_starts_on: typing.Optional[QueryConfigWeekStartsOn] = None
    provider_priority_overrides: typing.Optional[typing.List[QueryConfigProviderPriorityOverridesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow