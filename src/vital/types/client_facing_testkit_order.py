# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .client_facing_shipment import ClientFacingShipment
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingTestkitOrder(UniversalBaseModel):
    """
    Schema for a testkit order in the client facing API.

    To be used as part of a ClientFacingOrder.
    """

    id: str = pydantic.Field()
    """
    The Vital TestKit Order ID
    """

    shipment: typing.Optional[ClientFacingShipment] = pydantic.Field(default=None)
    """
    Shipment object
    """

    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
