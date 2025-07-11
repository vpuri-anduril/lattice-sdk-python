# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CronWindow(UniversalBaseModel):
    cron_expression: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="cronExpression")] = (
        pydantic.Field(default=None)
    )
    """
    in UTC, describes when and at what cadence this window starts, in the quartz flavor of cron
    
     examples:
        This schedule is begins at 7:00:00am UTC everyday between Monday and Friday
            0 0 7 ? * MON-FRI *
        This schedule begins every 5 minutes starting at 12:00:00pm UTC until 8:00:00pm UTC everyday
            0 0/5 12-20 * * ? *
        This schedule begins at 12:00:00pm UTC on March 2nd 2023
            0 0 12 2 3 ? 2023
    """

    duration_millis: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="durationMillis")] = (
        pydantic.Field(default=None)
    )
    """
    describes the duration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
