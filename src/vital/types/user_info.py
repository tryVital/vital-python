# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .address import Address
import typing
from .guarantor_details import GuarantorDetails
from .race import Race
from .ethnicity import Ethnicity
from .sexual_orientation import SexualOrientation
from .gender_identity import GenderIdentity
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UserInfo(UniversalBaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    dob: str
    address: Address
    medical_proxy: typing.Optional[GuarantorDetails] = None
    race: typing.Optional[Race] = None
    ethnicity: typing.Optional[Ethnicity] = None
    sexual_orientation: typing.Optional[SexualOrientation] = None
    gender_identity: typing.Optional[GenderIdentity] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
