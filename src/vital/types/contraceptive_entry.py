# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .contraceptive_entry_type import ContraceptiveEntryType
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ContraceptiveEntry(UniversalBaseModel):
    date: str
    type: ContraceptiveEntryType = pydantic.Field()
    """
    ℹ️ This enum is non-exhaustive.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
