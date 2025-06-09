import json
import time
from collections.abc import Iterator

from needlr.auth.auth import _FabricAuthentication
from needlr import _http
from needlr._http import FabricResponse
from needlr.models.item import Item
from needlr.models.connection import Connection

class _ConnectionClient():
    """

    [Reference](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections)

    ### Coverage

    * Create Connection > create_connection()

    """

    def __init__(self, auth:_FabricAuthentication, base_url):
        """
        Initializes a Role object.

        Args:
            auth (_FabricAuthentication): An instance of the _FabricAuthentication class.
            base_url (str): The base URL for the role.

        Returns:
            None
        """
        self._auth = auth
        self._base_url = base_url    

    # ## TODO
    # def create_connection(self, workspace_id:str, connection:Item) -> FabricResponse:
    #     """
    #     Create a Connection

    #     Creates a new connection in the specified workspace.

    #     Args:
    #         workspace_id (str): The ID of the workspace.
    #         connection (Item): The connection object to be created.

    #     Returns:
    #         FabricResponse: The response from the API.

    #     Reference:
    #     [Create Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/create-connection?tabs=HTTP)
    #     """
    #     body = json.dumps(connection.model_dump())
        
    #     return _http._post_http(
    #         url=f"{self._base_url}workspaces/{workspace_id}/connections"
    #         ,auth=self._auth
    #         ,body=body
    #     )
    

    def ls(self) -> Iterator[Item]:
        """
        List Connections

        Retrieves a list of connections in the specified workspace.

        Args:
            workspace_id (str): The ID of the workspace.
            **kwargs: Additional keyword arguments to be passed to the API.

        Yields:
            Item: An item object representing each connection retrieved.

        Returns:
            Iterator[Item]: An iterator of item objects.

        Reference:
        [Microsoft Documentation](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/list-connections?tabs=HTTP)
        """
        resp = _http._get_http_paged(
            url = self._base_url + f"connections",
            auth=self._auth,
            items_extract=lambda x:x["value"]
        )
        for page in resp:
            for item in page.items:
                yield Connection(**item)


    def delete(self, connection_id:str) -> FabricResponse:
        """
        Delete Connection

        Deletes a connection in the specified workspace.

        Args:
            connection_id (str): The ID of the connection to be deleted.

        Returns:
            FabricResponse: The response from the API.

        Reference:
        [Delete Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/delete-connection?tabs=HTTP)
        """
        resp = _http._delete_http(
            url=f"{self._base_url}connections/{connection_id}",
            auth=self._auth
        )

        return resp

    def get(self, connection_id:str) -> Connection:
        """
        Get Connection

        Retrieves a connection by its ID.

        Args:
            connection_id (str): The ID of the connection to retrieve.

        Returns:
            Connection: The retrieved connection object.

        Reference:
        [Get Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/get-connection?tabs=HTTP)
        """
        resp = _http._get_http(
            url=f"{self._base_url}connections/{connection_id}",
            auth=self._auth
        )
        
        return Connection(**resp.body)
    
    # def update(self, connection:Connection) -> FabricResponse:
    #     """
    #     Update Connection

    #     Updates an existing connection.

    #     Args:
    #         connection (Connection): The connection object to be updated.

    #     Returns:
    #         FabricResponse: The response from the API.

    #     Reference:
    #     [Update Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/update-connection?tabs=HTTP)
    #     """
    #     body = json.dumps(connection.model_dump())
        
    #     return _http._patch_http(
    #         url=f"{self._base_url}connections/{connection.id}",
    #         auth=self._auth,
    #         body=body
    #     )
    
    def ls_supported_connection_types(self) -> Iterator[str]:
        """
        List Supported Connection Types

        Retrieves a list of supported connection types.

        Yields:
            str: A string representing each supported connection type.

        Returns:
            Iterator[str]: An iterator of supported connection types.

        Reference:
        [List Supported Connection Types](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/list-supported-connection-types?tabs=HTTP)
        """
        resp = _http._get_http(
            url=f"{self._base_url}connections/supportedConnectionTypes",
            auth=self._auth,

        )
        
        return [_ for _ in resp.body["value"]]
