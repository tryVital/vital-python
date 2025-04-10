# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .client_facing_source import ClientFacingSource
import typing
from .client_facing_peak_expiratory_flow_rate_sample import ClientFacingPeakExpiratoryFlowRateSample
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GroupedPeakExpiratoryFlowRate(UniversalBaseModel):
    source: ClientFacingSource
    data: typing.List[ClientFacingPeakExpiratoryFlowRateSample]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
