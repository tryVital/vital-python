# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TimeSlot(UniversalBaseModel):
    booking_key: typing.Optional[str] = None
    start: str = pydantic.Field()
    """
    Time is in UTC
    """

    end: str = pydantic.Field()
    """
    Time is in UTC
    """

    expires_at: typing.Optional[str] = None
    price: float
    is_priority: bool
    num_appointments_available: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
