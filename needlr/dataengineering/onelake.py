"""Module providing Lakehouse functions."""

from needlr.auth.auth import _FabricAuthentication

import uuid

from needlr.models.onelake import Shortcut, Shortcut_Target, OneLakeDataAccessRole, ShortcutConflictPolicy, Shortcut_Create
from needlr.models.item import Item
from needlr import _http
from needlr._http import FabricResponse

from typing import Literal, List, Iterator
import json

class _OneLakeClient():
    """
    [Reference](https://learn.microsoft.com/en-us/rest/api/fabric/lakehouse/items)

    ### Coverage
    * Create shortcut
    """

    def __init__(self, auth: _FabricAuthentication, base_url):
        """
        Initializes a new instance of the Lakehouse class.

        Args:
            auth (_FabricAuthentication): The authentication object used for authentication.
            base_url (str): The base URL of the Lakehouse.

        """
        self._auth = auth
        self._base_url = base_url

    def ls_shortcuts(self, workspace_id:uuid.UUID, item_id:str, parent_path:str=None) -> Iterator[Shortcut]:
        """
        Creates a new lakehouse.

        Args:
            workspace_id (uuid.UUID): The workspace ID.
            display_name (str): The display name of the lakehouse.
            description (str): The description of the lakehouse.
            enableSchemas (bool): The enable schemas flag.

        Returns:
            lakehouse: The created lakehouse.

        Reference:
        [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/list-shortcuts?tabs=HTTP)
        """
        resp = _http._get_http_paged(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/shortcuts",
            auth=self._auth,
            items_extract=lambda x:x["value"],
        )

        for page in resp:
            for item in page.items:
                yield Shortcut(**item)
        

    def get_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_path:str, shortcut_name:str) -> Shortcut:
        """
        Creates a new lakehouse.

        Args:
            workspace_id (uuid.UUID): The workspace ID.
            display_name (str): The display name of the lakehouse.
            description (str): The description of the lakehouse.
            enableSchemas (bool): The enable schemas flag.

        Returns:
            lakehouse: The created lakehouse.

        Reference:
        [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/list-shortcuts?tabs=HTTP)
        """
        resp = _http._get_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/shortcuts/{shortcut_path}/{shortcut_name}",
            auth=self._auth,
            items_extract=lambda x:x["value"],
        )
        
        return resp
    

    # def create_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_path:str, shortcut_name:str, shortcut_target:Shortcut_Target, conflict_policy:ShortcutConflictPolicy=ShortcutConflictPolicy.CreateOrOverwrite) -> Shortcut:
    def create_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_definition:Shortcut_Create, conflict_policy:ShortcutConflictPolicy=ShortcutConflictPolicy.CreateOrOverwrite) -> Shortcut:
        """
        Creates a new shortcut.

        Args:
            workspace_id (uuid.UUID): The workspace ID.
            item_id (str): The display name of the lakehouse.
            shortcut_path (str): The description of the lakehouse.
            shortcut_name (bool): The enable schemas flag.

        Returns:
            lakehouse: The created lakehouse.

        Reference:
        [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/list-shortcuts?tabs=HTTP)
        """

        # body = {
        #     "name": shortcut_name,
        #     "path": shortcut_path,
        #     "target": {
        #         **shortcut_target
        #     }
        # }

        body = json.loads(shortcut_definition.model_dump_json())

        resp = _http._post_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/shortcuts?shortcutConflictPolicy={conflict_policy.value}",
            auth=self._auth,
            json=body
        )
        
        return resp
    

    def delete_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_path:str, shortcut_name:str) -> FabricResponse:
        """
        Deletes a shortcut.

        Args:
            workspace_id (uuid.UUID): The workspace ID.
            item_id (str): The display name of the lakehouse.
            shortcut_path (str): The description of the lakehouse.
            shortcut_name (bool): The enable schemas flag.

        Returns:
            lakehouse: The created lakehouse.

        Reference:
        [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/list-shortcuts?tabs=HTTP)
        """


        resp = _http._delete_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/shortcuts/{shortcut_path}/{shortcut_name}",
            auth=self._auth
        )
        return resp
    

    def ls_data_access_roles(self, workspace_id:uuid.UUID, item_id:str) -> Iterator[OneLakeDataAccessRole]:
        
        resp = _http._get_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/dataAccessRoles",
            auth=self._auth,
            items_extract=lambda x:x["value"]
        )

        for item in resp.body.get('value'):
            yield OneLakeDataAccessRole(**item)


    ## THIS DOES NOT WORK YET
    # def enable_data_access_security(self, workspace_id:uuid.UUID, item_id:str) -> Item:
    #     """
    #     Enables or disables data access security for a lakehouse.

    #     Args:
    #         workspace_id (uuid.UUID): The workspace ID.
    #         item_id (str): The display name of the lakehouse.

    #     Returns:
            
    #     Reference:
    #     [Enable Data Access Security]()
    #     """
        
    #     resp = _http._post_http(
    #         url = f"{self._base_url}workspaces/{workspace_id}/artifacts/{item_id}/security/enable",
    #         auth=self._auth
    #     )
        
    #     return resp.status_code


    def create_data_access_role(self, workspace_id:uuid.UUID, item_id:str, roles:List[OneLakeDataAccessRole], dry_run:bool=False) -> FabricResponse:
        """
        Creates a new data access role.

        Args:
            workspace_id (uuid.UUID): The workspace ID.
            item_id (str): The display name of the lakehouse.
            role_name (str): The name of the data access role.
            description (str): The description of the data access role.

        Returns:
            Item: The created data access role.

        Reference:
        [Create Data Access Role](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-data-access-security/create-or-update-data-access-roles?tabs=HTTP)
        """

        # This has to be the full list of permissions, not just the ones you want to set/update
        body_existing_roles = self.ls_data_access_roles(workspace_id, item_id)  # Get all the existing roles first
        
        body = {"value": []}
        for role in roles:
            body.get('value').append(role.model_dump())

        for role_existing in body_existing_roles:
            if role_existing.name not in [role.name for role in roles]:
                body['value'].append(role_existing.model_dump())
                
        resp = _http._put_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/dataAccessRoles{'' if not dry_run else '?dryRun=true'}",
            auth=self._auth,
            json=body
        )

        return resp.status_code
        

    
    ## This API does not work yet
    # def reset_shortcut_cache(self, workspace_id:uuid.UUID) -> Shortcut:
    #     """
    #     Deletes any cached files that were stored while reading from shortcuts.

    #     Args:
    #         workspace_id (uuid.UUID): The workspace ID.
    #         item_id (str): The display name of the lakehouse.
    #         shortcut_path (str): The description of the lakehouse.
    #         shortcut_name (bool): The enable schemas flag.

    #     Returns:
    #         lakehouse: The created lakehouse.

    #     Reference:
    #     [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/reset-shortcut-cache?tabs=HTTP)
    #     """


    #     resp = _http._post_http_long_running(
    #         url = f"{self._base_url}workspaces/{workspace_id}/onelake/resetShortcutCache",
    #         auth=self._auth
    #     )
        
    #     return resp
    
