# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert import Alert
from .component_health import ComponentHealth
from .health_connection_status import HealthConnectionStatus
from .health_health_status import HealthHealthStatus


class Health(UniversalBaseModel):
    """
    General health of the entity as reported by the entity.
    """

    connection_status: typing_extensions.Annotated[
        typing.Optional[HealthConnectionStatus], FieldMetadata(alias="connectionStatus")
    ] = pydantic.Field(default=None)
    """
    Status indicating whether the entity is able to communicate with Entity Manager.
    """

    health_status: typing_extensions.Annotated[
        typing.Optional[HealthHealthStatus], FieldMetadata(alias="healthStatus")
    ] = pydantic.Field(default=None)
    """
    Top-level health status; typically a roll-up of individual component healths.
    """

    components: typing.Optional[typing.List[ComponentHealth]] = pydantic.Field(default=None)
    """
    Health of individual components running on this Entity.
    """

    update_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updateTime")] = (
        pydantic.Field(default=None)
    )
    """
    The update time for the top-level health information.
     If this timestamp is unset, the data is assumed to be most recent
    """

    active_alerts: typing_extensions.Annotated[
        typing.Optional[typing.List[Alert]], FieldMetadata(alias="activeAlerts")
    ] = pydantic.Field(default=None)
    """
    Active alerts indicate a critical change in system state sent by the asset
     that must be made known to an operator or consumer of the common operating picture.
     Alerts are different from ComponentHealth messages--an active alert does not necessarily
     indicate a component is in an unhealthy state. For example, an asset may trigger
     an active alert based on fuel levels running low. Alerts should be removed from this list when their conditions
     are cleared. In other words, only active alerts should be reported here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
