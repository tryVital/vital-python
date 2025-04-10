# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .client_facing_source import ClientFacingSource
import typing
from .client_facing_sleep_apnea_alert_sample import ClientFacingSleepApneaAlertSample
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GroupedSleepApneaAlert(UniversalBaseModel):
    source: ClientFacingSource
    data: typing.List[ClientFacingSleepApneaAlertSample]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
