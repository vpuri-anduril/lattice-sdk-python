# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .enu import Enu
from .position import Position
from .quaternion import Quaternion


class Location(UniversalBaseModel):
    """
    Available for Entities that have a single or primary Location.
    """

    position: typing.Optional[Position] = pydantic.Field(default=None)
    """
    see Position definition for details.
    """

    velocity_enu: typing_extensions.Annotated[typing.Optional[Enu], FieldMetadata(alias="velocityEnu")] = (
        pydantic.Field(default=None)
    )
    """
    Velocity in an ENU reference frame centered on the corresponding position. All units are meters per second.
    """

    speed_mps: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="speedMps")] = pydantic.Field(
        default=None
    )
    """
    Speed is the magnitude of velocity_enu vector [sqrt(e^2 + n^2 + u^2)] when present, measured in m/s.
    """

    acceleration: typing.Optional[Enu] = pydantic.Field(default=None)
    """
    The entity's acceleration in meters/s^2.
    """

    attitude_enu: typing_extensions.Annotated[typing.Optional[Quaternion], FieldMetadata(alias="attitudeEnu")] = (
        pydantic.Field(default=None)
    )
    """
    quaternion to translate from entity body frame to it's ENU frame
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
