from pydantic import AliasChoices, Field, BaseModel
from typing import Any, Dict, Optional

from needlr.models.item import ItemType, Item


class Lakehouse(Item):
    name: str = Field(validation_alias=AliasChoices('displayName'))
    type: ItemType = ItemType.Lakehouse


class Livy_Session(BaseModel):
    sparkApplicationId: str = Field(validation_alias=AliasChoices('sparkApplicationId'))
    state: str = Field(validation_alias=AliasChoices('state'))
    livyId: str = Field(validation_alias=AliasChoices('livyId'))
    origin: str = Field(validation_alias=AliasChoices('origin'))
    attemptNumber: int = Field(validation_alias=AliasChoices('attemptNumber'))
    maxNumberOfAttempts: int = Field(validation_alias=AliasChoices('maxNumberOfAttempts'))
    livyName: str = Field(validation_alias=AliasChoices('livyName'))
    submitter: Optional[Dict] = Field(validation_alias=AliasChoices('submitter'))
    item: Optional[Dict] = Field(validation_alias=AliasChoices('item'))
    itemName: str = Field(validation_alias=AliasChoices('itemName'))
    itemType: str = Field(validation_alias=AliasChoices('itemType'))
    jobType: str = Field(validation_alias=AliasChoices('jobType'))
    submittedDateTime: str = Field(validation_alias=AliasChoices('submittedDateTime'))
    startDateTime: str = Field(validation_alias=AliasChoices('startDateTime'))
    endDateTime: str = Field(validation_alias=AliasChoices('endDateTime'))
    queuedDuration: Optional[Dict] = Field(validation_alias=AliasChoices('queuedDuration'))
    runningDuration: Optional[Dict] = Field(validation_alias=AliasChoices('runningDuration'))
    totalDuration: Optional[Dict] = Field(validation_alias=AliasChoices('totalDuration'))
    jobInstanceId: str = Field(validation_alias=AliasChoices('jobInstanceId'))
    creatorItem: Optional[Dict] = Field(validation_alias=AliasChoices('creatorItem'))
    cancellationReason: str | None = None
    capacityId: str = Field(validation_alias=AliasChoices('capacityId'))
    operationName: str = Field(validation_alias=AliasChoices('operationName'))
    runtimeVersion: str = Field(validation_alias=AliasChoices('runtimeVersion'))
    livySessionItemResourceUri: str | None = None

