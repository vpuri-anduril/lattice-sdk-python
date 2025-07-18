# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_of_view_mode import FieldOfViewMode
from .pose import Pose
from .position import Position
from .projected_frustum import ProjectedFrustum


class FieldOfView(UniversalBaseModel):
    """
    Sensor Field Of View closely resembling fov.proto SensorFieldOfView.
    """

    fov_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="fovId")] = pydantic.Field(
        default=None
    )
    """
    The Id for one instance of a FieldOfView, persisted across multiple updates to provide continuity during
     smoothing. This is relevant for sensors where the dwell schedule is on the order of
     milliseconds, making multiple FOVs a requirement for proper display of search beams.
    """

    mount_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mountId")] = pydantic.Field(
        default=None
    )
    """
    The Id of the mount the sensor is on.
    """

    projected_frustum: typing_extensions.Annotated[
        typing.Optional[ProjectedFrustum], FieldMetadata(alias="projectedFrustum")
    ] = pydantic.Field(default=None)
    """
    The field of view the sensor projected onto the ground.
    """

    projected_center_ray: typing_extensions.Annotated[
        typing.Optional[Position], FieldMetadata(alias="projectedCenterRay")
    ] = pydantic.Field(default=None)
    """
    Center ray of the frustum projected onto the ground.
    """

    center_ray_pose: typing_extensions.Annotated[typing.Optional[Pose], FieldMetadata(alias="centerRayPose")] = (
        pydantic.Field(default=None)
    )
    """
    The origin and direction of the center ray for this sensor relative to the ENU frame. A ray which is aligned with
     the positive X axis in the sensor frame will be transformed into the ray along the sensor direction in the ENU
     frame when transformed by the quaternion contained in this pose.
    """

    horizontal_fov: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="horizontalFov")] = (
        pydantic.Field(default=None)
    )
    """
    Horizontal field of view in radians.
    """

    vertical_fov: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="verticalFov")] = (
        pydantic.Field(default=None)
    )
    """
    Vertical field of view in radians.
    """

    range: typing.Optional[float] = pydantic.Field(default=None)
    """
    Sensor range in meters.
    """

    mode: typing.Optional[FieldOfViewMode] = pydantic.Field(default=None)
    """
    The mode that this sensor is currently in, used to display for context in the UI. Some sensors can emit multiple
     sensor field of views with different modes, for example a radar can simultaneously search broadly and perform
     tighter bounded tracking.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
