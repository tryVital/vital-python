# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .availability import Availability
import typing
from .scope_requirements_grants import ScopeRequirementsGrants
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ResourceAvailability(UniversalBaseModel):
    status: Availability
    scope_requirements: typing.Optional[ScopeRequirementsGrants] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
