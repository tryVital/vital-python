# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .physician_create_request_signature_image import PhysicianCreateRequestSignatureImage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PhysicianCreateRequest(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: typing.Optional[str]
    npi: str
    licensed_states: typing.Optional[typing.List[str]]
    signature_image: typing.Optional[PhysicianCreateRequestSignatureImage] = pydantic.Field(
        description="An image of the physician signature for health insurance billing"
    )

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
