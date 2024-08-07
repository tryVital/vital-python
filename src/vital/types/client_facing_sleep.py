# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_sleep_stream import ClientFacingSleepStream
from .client_facing_source import ClientFacingSource

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingSleep(pydantic.BaseModel):
    user_id: str = pydantic.Field(
        description="User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."
    )
    id: str
    date: dt.datetime = pydantic.Field(
        description="Date of the specified record, formatted as ISO8601 datetime string in UTC 00:00. Deprecated in favour of calendar_date."
    )
    calendar_date: str = pydantic.Field(
        description="Date of the sleep summary in the YYYY-mm-dd format. This generally matches the sleep end date."
    )
    bedtime_start: dt.datetime = pydantic.Field(description="UTC Time when the sleep period started")
    bedtime_stop: dt.datetime = pydantic.Field(description="UTC Time when the sleep period ended")
    timezone_offset: typing.Optional[int]
    duration: int = pydantic.Field(
        description="Total duration of the sleep period (sleep.duration = sleep.bedtime_end - sleep.bedtime_start)::seconds"
    )
    total: int = pydantic.Field(
        description="Total amount of sleep registered during the sleep period (sleep.total = sleep.rem + sleep.light + sleep.deep)::seconds"
    )
    awake: int = pydantic.Field(description="Total amount of awake time registered during the sleep period::seconds")
    light: int = pydantic.Field(description="Total amount of light sleep registered during the sleep period::seconds")
    rem: int = pydantic.Field(
        description="Total amount of REM sleep registered during the sleep period, minutes::seconds"
    )
    deep: int = pydantic.Field(
        description="Total amount of deep (N3) sleep registered during the sleep period::seconds"
    )
    score: typing.Optional[int]
    hr_lowest: typing.Optional[int]
    hr_average: typing.Optional[int]
    efficiency: typing.Optional[float]
    latency: typing.Optional[int]
    temperature_delta: typing.Optional[float]
    skin_temperature: typing.Optional[float]
    hr_dip: typing.Optional[float]
    average_hrv: typing.Optional[float]
    respiratory_rate: typing.Optional[float]
    source: ClientFacingSource = pydantic.Field(description="Source the data has come from.")
    sleep_stream: typing.Optional[ClientFacingSleepStream]

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
