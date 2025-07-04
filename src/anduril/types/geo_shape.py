# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .geo_ellipse import GeoEllipse
from .geo_ellipsoid import GeoEllipsoid
from .geo_line import GeoLine
from .geo_point import GeoPoint
from .geo_polygon import GeoPolygon


class GeoShape(UniversalBaseModel):
    """
    A component that describes the shape of a geo-entity.
    """

    point: typing.Optional[GeoPoint] = None
    line: typing.Optional[GeoLine] = None
    polygon: typing.Optional[GeoPolygon] = None
    ellipse: typing.Optional[GeoEllipse] = None
    ellipsoid: typing.Optional[GeoEllipsoid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
