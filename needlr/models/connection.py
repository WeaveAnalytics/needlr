from __future__ import annotations
from enum import Enum
import uuid
from pydantic import BaseModel, Field
from typing import List, Optional, Union, Literal


###
# List connections
# https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/list-connections?tabs=HTTP
###
class ConnectionDetails(BaseModel):
    type: str
    path: str


class CredentialDetails(BaseModel):
    credentialType: str
    singleSignOnType: str
    connectionEncryption: str
    skipTestConnection: bool


class Connection(BaseModel):
    id: uuid.UUID
    displayName: Optional[str] = None
    gatewayId: Optional[str]
    connectivityType: str
    connectionDetails: Optional[ConnectionDetails]
    privacyLevel: Optional[str]
    credentialDetails: Optional[CredentialDetails]




###
# Create connections
# https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/create-connection?tabs=HTTP
###
class Connection_PrivacyLevel(str, Enum):
    Organizational = 'Organizational'
    Private = 'Private'
    Public = 'Public'
    NoneType = 'None'

class Credential_Anonymous(str, Enum):
    credentialType = 'Anonymous'

class Credential_BasicCredentials(BaseModel):
    credentialType: str
    password: str
    username: str

class Credential_Key(BaseModel):
    credentialType: Literal['Key'] = 'Key'
    key: str

class Credential_ServicePrincipal(BaseModel):
    credentialType: str
    servicePrincipalClientId: uuid.UUID
    servicePrincipalSecret: str
    tenantId: uuid.UUID

class Credential_SharedAccessSignature(BaseModel):
    credentialType: Literal['SharedAccessSignature'] = 'SharedAccessSignature'
    token: str

class Credential_Windows(BaseModel):
    credentialType: Literal['Windows'] = 'Windows'
    password: str
    username: str

class Credential_WindowsWithoutImpersonation(BaseModel):
    credentialType: Literal['WindowsWithoutImpersonation'] = 'WindowsWithoutImpersonation'

class Credential_WorkspaceIdentity(BaseModel):
    credentialType: Literal['WorkspaceIdentity'] = 'WorkspaceIdentity'

class Credential_ConnectionDetailsBooleanParameter(BaseModel):
    dataType: Literal['Boolean'] = 'Boolean'
    name: str
    value: bool

class Credential_ConnectionDetailsDateParameter(BaseModel):
    dataType: Literal['Date'] = 'Date'
    name: str
    value: str

class Credential_ConnectionDetailsDateTimeParameter(BaseModel):
    dataType: Literal['Date'] = 'DateTime'
    name: str
    value: str

class Credential_ConnectionDetailsDateTimeZoneParameter(BaseModel):
    dataType: Literal['DateTimeZone'] = 'DateTimeZone'
    name: str
    value: str

class Credential_ConnectionDetailsDurationParameter(BaseModel):
    dataType: Literal['Duration'] = 'Duration'
    name: str
    value: str

class Credential_ConnectionDetailsNumberParameter(BaseModel):
    dataType: Literal['Number'] = 'Number'
    name: str
    value: float

class Credential_ConnectionDetailsTextParameter(BaseModel):
    dataType: Literal['Text'] = 'Text'
    name: str 
    value: str

class Credential_ConnectionDetailsTimeParameter(BaseModel):
    dataType: Literal['Time'] = 'Time'
    name: str 
    value: str

class Connection_Encryption(str, Enum):
    Any = 'Any'
    Encrypted = 'Encrypted'
    NotEncrypted = 'NotEncrypted'

class DataType(str, Enum):
    Boolean = 'Boolean'
    Date = 'Date'
    DateTime = 'DateTime'
    DateTimeZone = 'DateTimeZone'
    Duration = 'Duration'
    Number = 'Number'
    Text = 'Text'
    Time = 'Time'

class Connection_ConnectivityType(str, Enum):
    Automatic = 'Automatic'
    OnPremisesGateway = 'OnPremisesGateway'
    OnPremisesGatewayPersonal = 'OnPremisesGatewayPersonal'
    PersonalCloud = 'PersonalCloud'
    ShareableCloud = 'ShareableCloud'
    VirtualNetworkGateway = 'VirtualNetworkGateway'
    NoneType = 'None'

class Credential_SingleSignOnType(str, Enum):
    Kerberos = 'Kerberos'
    KerberosDirectQueryAndRefresh = 'KerberosDirectQueryAndRefresh'
    MicrosoftEntraID = 'MicrosoftEntraID'
    NoneType = 'None'
    SecurityAssertionMarkupLanguage = 'SecurityAssertionMarkupLanguage'
    
class Connection_ConnectionDetails(BaseModel):
    creationMethod: str # ls_supported_connection_types()
    parameters: List[Union[Credential_ConnectionDetailsBooleanParameter, Credential_ConnectionDetailsDateParameter
                        , Credential_ConnectionDetailsDateTimeParameter
                        , Credential_ConnectionDetailsDateTimeZoneParameter, Credential_ConnectionDetailsDurationParameter
                        , Credential_ConnectionDetailsNumberParameter, Credential_ConnectionDetailsTextParameter
                        , Credential_ConnectionDetailsTimeParameter]]
    singleSignOnType: Credential_SingleSignOnType
    skipTestConnection: bool

class Credential_Create_CredentialDetails(BaseModel):
    connectionEncryption: Connection_Encryption
    credentials: Union[Credential_Anonymous, Credential_BasicCredentials, Credential_Key
                       , Credential_ServicePrincipal, Credential_SharedAccessSignature
                       , Credential_Windows, Credential_WindowsWithoutImpersonation
                       , Credential_WorkspaceIdentity]
    singleSignOnType: Credential_SingleSignOnType
    skipTestConnection: bool

class Credential_Type(str, Enum):
    Anonymous = 'Anonymous'
    Basic = 'Basic'
    Key = 'Key'
    OAuth2 = 'OAuth2'
    ServicePrincipal = 'ServicePrincipal'
    SharedAccessSignature = 'SharedAccessSignature'
    Windows = 'Windows'
    WindowsWithoutImpersonation = 'WindowsWithoutImpersonation'
    WorkspaceIdentity = 'WorkspaceIdentity'

class Connection_ListDetails(BaseModel):
    path: str
    type: str

class Credential_ListDetails(BaseModel):
    connectionEncryption: Connection_Encryption
    credentialType: Credential_Type
    SingleSignOnType: Credential_SingleSignOnType
    skipTestConnection: bool


class Credential_OnPremEntry(BaseModel):
    encryptedCredentials: str
    gatewayId: uuid.UUID

class Credential_Create_OnPremGateway(BaseModel):
    credentialType: Credential_Type
    values: str 

class Credential_Create_OnPremCredentialDetails(BaseModel):
    connectionEncryption: Optional[Connection_Encryption]
    credentials: Union[Credential_Anonymous, Credential_BasicCredentials, Credential_Key
                       , Credential_ServicePrincipal, Credential_SharedAccessSignature
                       , Credential_Windows, Credential_WindowsWithoutImpersonation
                       , Credential_WorkspaceIdentity]
    singleSignOnType: Credential_SingleSignOnType
    skipTestConnection: bool


class Connection_Create_CloudRequest(BaseModel):
    connectionDetails: Connection_ConnectionDetails
    connectivityType: str = Field(default=Connection_ConnectivityType.ShareableCloud, Literal=True)
    credentialDetails: Credential_Create_CredentialDetails
    displayName: str
    privacyLevel: Optional[Connection_PrivacyLevel] = Connection_PrivacyLevel.Organizational

class Connection_Create_OnPremRequest(BaseModel):
    connectionDetails: Connection_ConnectionDetails
    connectivityType: str = Field(default=Connection_ConnectivityType.OnPremisesGateway, Literal=True)
    credentialDetails: Credential_Create_CredentialDetails
    displayName: str
    gatewayId: uuid.UUID
    privacyLevel: Optional[Connection_PrivacyLevel] = Connection_PrivacyLevel.Organizational

class Connection_Create_VNetGatewayRequest(BaseModel):
    connectionDetails: Connection_ConnectionDetails
    connectivityType: str = Field(default=Connection_ConnectivityType.VirtualNetworkGateway, Literal=True)
    credentialDetails: Connection_ConnectionDetails
    displayName: str
    gatewayId: uuid.UUID
    privacyLevel: Optional[Connection_PrivacyLevel] = Connection_PrivacyLevel.Organizational




###
# Role Assignment
# https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/add-connection-role-assignment?tabs=HTTP#principal
###
# class Role_PrincipalType(str, Enum):
#     User =

class Role_ConnectionRole(str, Enum):
    Owner = 'Owner'
    User = 'User'
    UserWithReshare = 'UserWithReshare'

class Role_GroupType(str, Enum):
    DistributionList = 'DistributionList'
    SecurityGroup = 'SecurityGroup'
    Unknown = 'Unknown'

class Role_GroupDetails(BaseModel):
    groupType: Role_GroupType

class Role_ServicePrincipalDetails(BaseModel):
    aadAppId: uuid.UUID

class Role_ServicePrincipalProfileDetails(BaseModel):
    parentPrincipal: Role_Principal

class Role_PrincipalType(str, Enum):
    Group = 'Group'
    ServicePrincipal = 'ServicePrincipal'
    ServicePrincipalProfile = 'ServicePrincipalProfile'
    User = 'User'

class Role_UserDetails(BaseModel):
    userPrincipalName: str

class Role_Principal(BaseModel):
    displayName: str
    groupDetails: Role_GroupDetails
    id: uuid.UUID
    servicePrincipalDetails: Role_ServicePrincipalDetails
    servicePrincipalProfileDetails: Role_ServicePrincipalProfileDetails
    type: Role_PrincipalType
    userDetails: Role_UserDetails

class Role_Add_ConnectionRoleAssignmentRequest(BaseModel):
    principal: Role_Principal  
    role: Role_ConnectionRole  

