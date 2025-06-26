import uuid
from pydantic import BaseModel, Field, AliasChoices, computed_field, create_model
from typing import Union, Optional, List, Literal
from enum import Enum


class ShortcutConflictPolicy(str, Enum):
    Abort = 'Abort'
    CreateOrOverwrite = 'CreateOrOverwrite'
    GenerateUniqueName = 'GenerateUniqueName'
    OverwriteOnly = 'OverwriteOnly'


class Shortcut_AdlsGen2(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_AmazonS3(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_AzureBlobStorage(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_Dataverse(BaseModel):
    connectionId:uuid.UUID
    deltaLakeFolder:str
    environmentDomain:str
    tableName:str

class Shortcut_GoogleCloudStorage(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_OneLake(BaseModel):
    itemId:uuid.UUID
    path:str
    workspaceId:uuid.UUID


class Shortcut_S3Compatible(BaseModel):
    bucket:str
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_Dataverse(BaseModel):
    connectionId:uuid.UUID
    deltaLakeFolder:str
    environmentDomain:str
    tableName:str




class Shortcut_Target_AdlsGen2(BaseModel):
    adlsGen2: Shortcut_AdlsGen2

class Shortcut_Target_AmazonS3(BaseModel):
    amazonS3: Shortcut_AmazonS3

class Shortcut_Target_AzureBlobStorage(BaseModel):
    azureBlobStorage: Shortcut_AzureBlobStorage

class Shortcut_Target_Dataverse(BaseModel):
    dataverse: Shortcut_Dataverse

class Shortcut_Target_GoogleCloudStorage(BaseModel):
    googleCloudStorage: Shortcut_GoogleCloudStorage

class Shortcut_Target_OneLake(BaseModel):
    oneLake: Shortcut_OneLake

class Shortcut_Target_S3Compatible(BaseModel):
    s3Compatible: Shortcut_S3Compatible


class Shortcut_Create(BaseModel):
    path: str
    name: str
    target: Union[Shortcut_Target_AdlsGen2, Shortcut_Target_AmazonS3, Shortcut_Target_AzureBlobStorage
                  , Shortcut_Target_Dataverse, Shortcut_Target_GoogleCloudStorage
                  , Shortcut_Target_OneLake, Shortcut_Target_S3Compatible]


class Shortcut_Target(BaseModel):
    type: str
    adlsGen2:Optional[Shortcut_AdlsGen2] = None 
    amazonS3:Optional[Shortcut_AmazonS3] = None 
    azureBlobStorage:Optional[Shortcut_AzureBlobStorage] = None 
    dataverse:Optional[Shortcut_Dataverse] = None 
    externalDataShare:Optional[Shortcut_Dataverse] = None 
    googleCloudStorage:Optional[Shortcut_GoogleCloudStorage] = None 
    oneLake:Optional[Shortcut_OneLake] = None 
    s3Compatible:Optional[Shortcut_S3Compatible] = None 



class Shortcut(BaseModel):
    path:str
    name:str
    target:Shortcut_Target


class Shortcut_Target_Create_OneLake(BaseModel):
    itemId:uuid.UUID
    path:str
    workspaceId:uuid.UUID


class Shortcut_Target_Create_AdlsGen2(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_Target_Create_AmazonS3(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str


class Shortcut_Target_Create_AzureBlobStorage(BaseModel):
    connectionId:uuid.UUID
    location:str
    subpath:str



class ObjectType(str, Enum):
    Group = 'Group'
    ManagedIdentity = 'ManagedIdentity'
    ServicePrincipal = 'ServicePrincipal'
    User = 'User'
    NoneType = 'None'


class ItemAccess(str, Enum):
    Execute = 'Execute'
    Explore = 'Explore'
    Read = 'Read'
    ReadAll = 'ReadAll'
    Reshare = 'Reshare'
    Write = 'Write'


class AttributeName(str, Enum):
    Action = 'Action'
    Path = 'Path'


class Effect(str, Enum):
    Permit = 'Permit'
    # Deny = 'Deny'


class PermissionItem(BaseModel):
    attributeName: AttributeName
    attributeValueIncludedIn: List[str]


class DecisionRule(BaseModel):
    effect: Effect
    permission: List[PermissionItem]


class FabricItemMember(BaseModel):
    itemAccess: List[ItemAccess]
    sourcePath: str


class MicrosoftEntraMember(BaseModel):
    objectId: Optional[str] = None
    objectType: Optional[ObjectType] = None
    tenantId: Optional[str] = None


class Members(BaseModel):
    fabricItemMembers: Optional[List[FabricItemMember]] = []
    microsoftEntraMembers: Optional[List[MicrosoftEntraMember]] = []


class OneLakeDataAccessRole(BaseModel):
    name: str
    decisionRules: List[DecisionRule]
    members: Members


