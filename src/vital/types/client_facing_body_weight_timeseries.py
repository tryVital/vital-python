# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingBodyWeightTimeseries(pydantic.BaseModel):
    id: typing.Optional[int]
    timezone_offset: typing.Optional[int]
    type: typing.Optional[str]
    unit: str = pydantic.Field(description="Measured in kilograms (kg).")
    timestamp: dt.datetime = pydantic.Field(description="The timestamp of the measurement.")
    value: float = pydantic.Field(description="The value of the measurement.")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
