# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContentIdentifier(UniversalBaseModel):
    path: str = pydantic.Field()
    """
    A valid path must not contain the following:
    - Spaces or Tabs
    - Special characters other than underscore (_), dash (-), period (.) and slash (/)
    - Non-ASCII characters such as accents or symbols
    Paths must not start with a leading space.
    """

    checksum: str = pydantic.Field()
    """
    The SHA-256 checksum of this object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
