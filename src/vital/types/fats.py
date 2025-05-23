# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Fats(UniversalBaseModel):
    saturated: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of saturated fats in grams (g)
    """

    monounsaturated: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of monounsaturated fats in grams (g)
    """

    polyunsaturated: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of polyunsaturated fats in grams (g)
    """

    omega_3: typing.Optional[float] = pydantic.Field(alias="omega3", default=None)
    """
    Amount of Omega-3 fatty acids in grams (g)
    """

    omega_6: typing.Optional[float] = pydantic.Field(alias="omega6", default=None)
    """
    Amount of Omega-6 fatty acids in grams (g)
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total amount of fats in grams (g)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
