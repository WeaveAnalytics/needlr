"""Module providing Lakehouse functions."""

from needlr.auth.auth import _FabricAuthentication

import uuid

from needlr.models.onelake import Shortcut, Shortcut_Target
from needlr.models.item import Item
from needlr import _http
from needlr._http import FabricResponse

from typing import Literal

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

    def ls_shortcuts(self, workspace_id:uuid.UUID, item_id:str, parent_path:str=None) -> Shortcut:
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
    

    def create_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_path:str, shortcut_name:str, target:Shortcut_Target) -> Shortcut:
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

        body = {
            "name": shortcut_name,
            "path": shortcut_path,
            "target": {
                **target
            }
        }

        resp = _http._post_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/shortcuts?shortcutConflictPolicy=CreateOrOverwrite",
            auth=self._auth,
            json=body
        )
        
        return resp
    

    def delete_shortcut(self, workspace_id:uuid.UUID, item_id:str, shortcut_path:str, shortcut_name:str) -> Shortcut:
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
    #     [List shortcuts](https://learn.microsoft.com/en-us/rest/api/fabric/core/onelake-shortcuts/list-shortcuts?tabs=HTTP)
    #     """


    #     resp = _http._post_http_long_running(
    #         url = f"{self._base_url}workspaces/{workspace_id}/onelake/resetShortcutCache",
    #         auth=self._auth
    #     )
        
    #     return resp
    
