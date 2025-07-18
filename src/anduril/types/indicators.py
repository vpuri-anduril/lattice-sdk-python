# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Indicators(UniversalBaseModel):
    """
    Indicators to describe entity to consumers.
    """

    simulated: typing.Optional[bool] = None
    exercise: typing.Optional[bool] = None
    emergency: typing.Optional[bool] = None
    c_2: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="c2")] = None
    egressable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates the Entity should be egressed to external sources.
     Integrations choose how the egressing happens (e.g. if an Entity needs fuzzing).
    """

    starred: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A signal of arbitrary importance such that the entity should be globally marked for all users
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
