# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
from .order_status import OrderStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ClientFacingOrderEvent(UniversalBaseModel):
    id: int
    created_at: dt.datetime
    status: OrderStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
