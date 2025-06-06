from enum import Enum
import uuid
from pydantic import BaseModel
from typing import List, Optional

class ConnectionDetails(BaseModel):
    type: str
    path: str


class CredentialDetails(BaseModel):
    credentialType: str
    singleSignOnType: str
    connectionEncryption: str
    skipTestConnection: bool


class Connection(BaseModel):
    id: str
    displayName: Optional[str] = None
    gatewayId: Optional[str]
    connectivityType: str
    connectionDetails: Optional[ConnectionDetails]
    privacyLevel: Optional[str]
    credentialDetails: Optional[CredentialDetails]




# class Parameter(BaseModel):
#     dataType: str
#     name: str
#     value: str


# class ConnectionDetails(BaseModel):
#     type: str
#     creationMethod: str
#     parameters: List[Parameter]


# class Credentials(BaseModel):
#     credentialType: str
#     username: str
#     password: str


# class CredentialDetails(BaseModel):
#     singleSignOnType: str
#     connectionEncryption: str
#     skipTestConnection: bool
#     credentials: Credentials


# class Model(BaseModel):
#     connectivityType: str
#     displayName: str
#     connectionDetails: ConnectionDetails
#     privacyLevel: str
#     credentialDetails: CredentialDetails