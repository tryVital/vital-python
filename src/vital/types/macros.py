# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fats import Fats


class Macros(UniversalBaseModel):
    carbs: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of carbohydrates in grams (g)
    """

    protein: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of protein in grams (g)
    """

    fats: typing.Optional[Fats] = pydantic.Field(default=None)
    """
    Details of fat content
    """

    alcohol: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of alcohol in grams (g)
    """

    water: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of water in grams (g)
    """

    fibre: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of dietary fiber in grams (g)
    """

    sugar: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of sugar in grams (g)
    """

    cholesterol: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of cholesterol in grams (g)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
