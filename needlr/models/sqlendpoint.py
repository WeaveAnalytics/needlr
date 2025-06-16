
import uuid

from pydantic import AliasChoices, BaseModel, Field
from enum import Enum
from typing import Optional
from needlr.models.item import ItemType, Item


class SQLEndpoint(Item):
    name: str = Field(validation_alias=AliasChoices('displayName'))
    type: ItemType = ItemType.SQLEndpoint

class SyncStatus(str, Enum):
    Failure = "Failure"
    NotRun = "NotRun"
    Success = "Success"

class TimeUnit(str, Enum):
    Days = "Days"
    Hours = "Hours"
    Minutes = "Minutes"
    Seconds = "Seconds"

class Duration(BaseModel):
    timeUnit: TimeUnit
    value: int

class SqlEndpointRefreshMetadata(BaseModel):
    timeout: Duration = Field(default=Duration(timeUnit=TimeUnit.Minutes, value=15))

class TableSyncStatus(BaseModel):
    endDateTime: str # The date and time when the table synchronization completed in UTC, using the YYYY-MM-DDTHH:mm:ssZ format.
    error: Optional[str]
    lastSuccessfulSyncDateTime: str # The date and time when the table synchronization was successful in UTC, using the YYYY-MM-DDTHH:mm:ssZ format.
    startDateTime: str # The date and time when the table synchronization started in UTC, using the YYYY-MM-DDTHH:mm:ssZ format.
    status: SyncStatus
    tableName: str



