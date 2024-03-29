# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LabResultsMetadata(pydantic.BaseModel):
    age: str
    dob: str
    clia: typing.Optional[str] = pydantic.Field(alias="clia_#")
    patient: str
    provider: typing.Optional[str]
    laboratory: typing.Optional[str]
    date_reported: str
    date_collected: typing.Optional[str]
    specimen_number: str
    date_received: typing.Optional[str]
    status: typing.Optional[str]
    interpretation: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
