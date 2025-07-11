# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .position import Position


class GeoPolygonPosition(UniversalBaseModel):
    """
    A position in a GeoPolygon with an optional extruded height.
    """

    position: typing.Optional[Position] = pydantic.Field(default=None)
    """
    base position. if no altitude set, its on the ground.
    """

    height_m: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="heightM")] = pydantic.Field(
        default=None
    )
    """
    optional height above base position to extrude in meters.
     for a given polygon, all points should have a height or none of them.
     strictly GeoJSON compatible polygons will not have this set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
