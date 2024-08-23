# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .company_details import CompanyDetails
from .person_details_output import PersonDetailsOutput
from .responsible_relationship import ResponsibleRelationship

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingInsurance(pydantic.BaseModel):
    member_id: str
    payor_code: str
    relationship: ResponsibleRelationship
    insured: PersonDetailsOutput
    company: CompanyDetails
    group_id: typing.Optional[str]
    guarantor: typing.Optional[PersonDetailsOutput]

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