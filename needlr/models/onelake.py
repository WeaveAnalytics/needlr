import uuid
from pydantic import BaseModel, Field, AliasChoices, computed_field, create_model
from typing import Dict, Union, Optional


# Union[ModelA, ModelB]


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


class Shortcut_ExternalDataShare(BaseModel):
    connectionId:uuid.UUID


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



# class Shortcut_Target_Create(BaseModel):
#     # oneLake:Shortcut_Target_OneLake_Create
#     oneLake: create_model('itemId')
#     # daytime: Optional[create_model('DayTime', sunrise=(int, ...), sunset=(int, ...))] = None


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


# class Shortcut_Target_OneLake(BaseModel):
#     type: str
#     oneLake:Optional[Shortcut_OneLake]

class Shortcut(BaseModel):
    path:str
    name:str
    # target:Union[Shortcut_AdlsGen2] # = Field(validation_alias=AliasChoices('target'))
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


    
    # @computed_field
    # @property
    # def target(self) -> Shortcut_Target_OneLake: #Union[Shortcut_Target_OneLake]:
    #     # if values.data.get('type') == 'adlsGen2':
    #     #     return Shortcut_AdlsGen2(**values)
    #     # elif values.data.get('type') == 'amazonS3':
    #     #     return Shortcut_AmazonS3(**values)
    #     # elif values.data.get('type') == 'azureBlobStorage':
    #     #     return Shortcut_AzureBlobStorage(**values)
    #     # elif values.data.get('type') == 'dataverse':
    #     #     return Shortcut_Dataverse(**values)
    #     # elif values.data.get('type') == 'externalDataShare':
    #     #     return Shortcut_ExternalDataShare(**values)
    #     # elif values.data.get('type') == 'googleCloudStorage':
    #         # return Shortcut_GoogleCloudStorage(**values)
    #     if self.target.get('type') == 'oneLake':
    #         return Shortcut_Target_OneLake(self.target)
    #     # elif values.data.get('type') == 's3Compatible':
    #     #     return Shortcut_S3Compatible(**values)