# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .line_of_bearing import LineOfBearing
from .u_int_32_range import UInt32Range


class Tracked(UniversalBaseModel):
    """
    Available for Entities that are tracked.
    """

    track_quality_wrapper: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="trackQualityWrapper")
    ] = pydantic.Field(default=None)
    """
    Quality score, 0-15, nil if none
    """

    sensor_hits: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sensorHits")] = pydantic.Field(
        default=None
    )
    """
    Sensor hits aggregation on the tracked entity.
    """

    number_of_objects: typing_extensions.Annotated[
        typing.Optional[UInt32Range], FieldMetadata(alias="numberOfObjects")
    ] = pydantic.Field(default=None)
    """
    Estimated number of objects or units that are represented by this entity. Known as Strength in certain contexts (Link16)
     if UpperBound == LowerBound; (strength = LowerBound)
     If both UpperBound and LowerBound are defined; strength is between LowerBound and UpperBound (represented as string "Strength: 4-5")
     If UpperBound is defined only (LowerBound unset), Strength ≤ UpperBound
     If LowerBound is defined only (UpperBound unset), LowerBound ≤ Strength
     0 indicates unset.
    """

    radar_cross_section: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="radarCrossSection")
    ] = pydantic.Field(default=None)
    """
    The radar cross section (RCS) is a measure of how detectable an object is by radar. A large RCS indicates an object is more easily
     detected. The unit is “decibels per square meter,” or dBsm
    """

    last_measurement_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastMeasurementTime")
    ] = pydantic.Field(default=None)
    """
    Timestamp of the latest tracking measurement for this entity.
    """

    line_of_bearing: typing_extensions.Annotated[
        typing.Optional[LineOfBearing], FieldMetadata(alias="lineOfBearing")
    ] = pydantic.Field(default=None)
    """
    The relative position of a track with respect to the entity that is tracking it. Used for tracks that do not yet have a 3D position.
     For this entity (A), being tracked by some entity (B), this LineOfBearing would express a ray from B to A.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
