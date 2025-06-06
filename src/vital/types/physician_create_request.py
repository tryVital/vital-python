# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .physician_create_request_signature_image import PhysicianCreateRequestSignatureImage


class PhysicianCreateRequest(UniversalBaseModel):
    first_name: str
    last_name: str
    email: typing.Optional[str] = None
    npi: str
    licensed_states: typing.Optional[typing.List[str]] = None
    signature_image: typing.Optional[PhysicianCreateRequestSignatureImage] = pydantic.Field(default=None)
    """
    An image of the physician signature for health insurance billing
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
