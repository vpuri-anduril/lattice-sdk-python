# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .linear_ring import LinearRing


class GeoPolygon(UniversalBaseModel):
    """
    A polygon shaped geo-entity.
     See https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.6, only canonical representations accepted
    """

    rings: typing.Optional[typing.List[LinearRing]] = pydantic.Field(default=None)
    """
    An array of LinearRings where the first item is the exterior ring and subsequent items are interior rings.
    """

    is_rectangle: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isRectangle")] = (
        pydantic.Field(default=None)
    )
    """
    An extension hint that this polygon is a rectangle. When true this implies several things:
     * exactly 1 linear ring with 5 points (starting corner, 3 other corners and start again)
     * each point has the same altitude corresponding with the plane of the rectangle
     * each point has the same height (either all present and equal, or all not present)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
