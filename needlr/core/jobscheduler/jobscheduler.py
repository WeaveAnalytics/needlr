"""Module providing Core Job Scheduling functions."""

from collections.abc import Iterator
from needlr import _http
from needlr._http import FabricResponse
import uuid
from needlr.auth.auth import _FabricAuthentication
#from needlr._http import FabricResponse, FabricException
from needlr.models.jobscheduler import ( ItemSchedules, CreateScheduleRequest, ItemJobInstance)


#import json
#from pydantic import BaseModel
#import uuid

class _JobSchedulerClient():
    """

    [_JobSchedulerClient](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler)

    Methods:
    cancel_item_job_instance - Cancel an item's job instance.
    create_item_schedule_Cron - Create a new schedule for an item.
    get_item_job_instance - Get one item's job instance.
    get_item_schedule - Get an existing schedule for an item.
    list_item_job_instances - Returns a list of job instances for the specified item.
    list_item_schedules - Get scheduling settings for one specific item.
    run_on_demand_item_job - Run on-demand item job instance.
    update_item_schedule - Update an existing schedule for an item.

    """

    def __init__(self, auth: _FabricAuthentication, base_url):
        """
        Initializes a _JobSchedulerClient object.

        Args:
            auth (_FabricAuthentication): An instance of the _FabricAuthentication class.
            base_url (str): The base URL for the role.

        Returns:
            None
        """
        self._auth = auth
        self._base_url = base_url

    def list_item_schedules(self, workspace_id:uuid.UUID, item_id:uuid.UUID, job_type:str, **kwargs) -> Iterator[ItemSchedules]:
            """
            Get scheduling settings for one specific item.

            Currently supported job types:
            - RunNotebook
            - Pipeline

            Future support for:
            - SparkJob

            Parameters:
                workspace_id (uuid.UUID): The ID of the workspace.
                item_id (uuid.UUID): The ID of the item.
                job_type (str): The type of job. Must be either "RunNotebook" or "Pipeline".

            Returns:
                Iterator[ItemSchedules]: An iterator that yields Workspace objects representing each ItemSchedule.

            Reference:
            - [List Item Schedules](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler/list-item-schedules?tabs=HTTP)
            """

            # Check that job_type is RunNotebook or Pipeline
            if job_type not in ["RunNotebook", "Pipeline"]:
                raise ValueError("job_type must be either 'RunNotebook' or 'Pipeline'")

            # Check that workspace_id and item_id are valid UUIDs
            if not isinstance(workspace_id, uuid.UUID) or not isinstance(item_id, uuid.UUID):
                raise ValueError("workspace_id and item_id must be valid UUIDs")

            resp = _http._get_http_paged(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/jobs/{job_type}/schedules",
            auth= self._auth,
            items_extract=lambda x:x["value"],
            **kwargs 
            )

            for page in resp:
                for item in page.items:
                    yield ItemSchedules(**item)

    def create_item_schedule_cron( self, item_id: uuid.UUID, 
                        job_type: str, 
                        workspace_id: uuid.UUID,
                        endDateTime: str,
                        interval: int,
                        localTimeZoneId: str,
                        startDateTime: str,
                        enabled: bool,
                        **kwargs) -> FabricResponse:
        """
        Create a new schedule for an item.

        Currently supported job types:
        - RunNotebook
        - Pipeline

        Parameters:
        - item_id: The item ID.
        - job_type:  The job type.
        - workspace_id:  The workspace ID.
        - endDateTime: The end time for this schedule. The end time must be later than the start time.
        - interval: The time interval in minutes. A number between 1 and 5270400 (10 years).
        - localTimeZoneId: The time zone identifier registry on local computer for windows, see Default Time Zones(https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones?view=windows-11)
        - startDateTime: The start time for this schedule. If the start time is in the past, it will trigger a job instantly.
        - enabled: A boolean indicating whether the schedule is enabled.

        Reference:
        - [Create Item Schedule](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler/create-item-schedule?tabs=HTTP)
        """

        # Check that job_type is RunNotebook or Pipeline
        if job_type not in ["RunNotebook", "Pipeline"]:
            raise ValueError("job_type must be either 'RunNotebook' or 'Pipeline'")

        # Check that workspace_id and item_id are valid UUIDs
        if not isinstance(workspace_id, uuid.UUID) or not isinstance(item_id, uuid.UUID):
            raise ValueError("workspace_id and item_id must be valid UUIDs")

        # create the VirtualNetworkAzureResource object
        cronVar = {"endDateTime":endDateTime, "interval":interval, "localTimeZoneId":localTimeZoneId,  "startDateTime":startDateTime, "type":"Cron"}

        body = {"enabled": enabled, 
                "configuration": cronVar}
        
        url=f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/jobs/{job_type}/schedules"

        resp = _http._post_http(
            url=url,
            auth=self._auth,
            item=CreateScheduleRequest(**body),
        )

        
        return resp
    
    def cancel_item_job_instance(self, workspace_id:uuid.UUID, item_id:uuid.UUID, job_instance_id:uuid.UUID) -> FabricResponse:
        """
        Cancel an item's job instance.

        Args:
            workspace_id (uuid.UUID): The ID of the workspace.
            item_id (uuid.UUID): The item ID.
            job_instance_id (uuid.UUID): The job instance ID.

        Returns:
            FabricResponse: The response from the delete request.

        Reference:
        - [Cancel Item Job Instance](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler/cancel-item-job-instance?tabs=HTTP)
        """

        # Check that workspace_id and item_id are valid UUIDs
        if not isinstance(workspace_id, uuid.UUID) or not isinstance(item_id, uuid.UUID) or not isinstance(job_instance_id, uuid.UUID):
            raise ValueError("workspace_id, item_id, job_instance_id must be valid UUIDs")
                
        resp = _http._post_http(
            url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/jobs/instances/{job_instance_id}/cancel",
            auth=self._auth
        )
        return resp
    

    def list_item_job_instances(self, workspace_id:uuid.UUID, item_id:uuid.UUID, **kwargs) -> Iterator[ItemJobInstance]:
            """
            Returns a list of job instances for the specified item.

            Parameters:
                workspace_id (uuid.UUID): The ID of the workspace.
                item_id (uuid.UUID): The ID of the item.

            Returns:
                Iterator[ItemJobInstances]: An iterator that yields Workspace objects representing each ItemJobInstance.

            Reference:
            - [List Item Job Instancens](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler/list-item-job-instances?tabs=HTTP)
            """

            # Check that workspace_id and item_id are valid UUIDs
            if not isinstance(workspace_id, uuid.UUID) or not isinstance(item_id, uuid.UUID):
                raise ValueError("workspace_id and item_id must be valid UUIDs")

            resp = _http._get_http(
                url = f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/jobs/instances",
                auth= self._auth,
                **kwargs
            )

            # convert the None to 'None' for the response due to the impedence mismatch between the API and the model
            # None va 'None'
            # TODO: Find a better way of handling this and document this needed.
            for k,v in resp.body.items():
                if v is None:
                    resp.body[k] = 'None'

            return ItemJobInstance(**resp.body)                        

    def run_on_demand_item_job( self, workspace_id:uuid.UUID, item_id:uuid.UUID, job_type:str) -> FabricResponse:
        """
        Run on-demand item job instance.

        Currently supported job types:
        - RunNotebook
        - Pipeline

        Future support for:
        - SparkJob

        Parameters:
            workspace_id (uuid.UUID): The ID of the workspace.
            item_id (uuid.UUID): The ID of the item.
            job_type (str): The type of job. Must be either "RunNotebook" or "Pipeline".

        Returns:
            Iterator[ItemSchedules]: An iterator that yields Workspace objects representing each ItemSchedule.

        Reference:
        - [List Item Schedules](https://learn.microsoft.com/en-us/rest/api/fabric/core/job-scheduler/list-item-schedules?tabs=HTTP)
        """

        # Check that job_type is RunNotebook or Pipeline
        if job_type not in ["RunNotebook", "Pipeline"]:
            raise ValueError("job_type must be either 'RunNotebook' or 'Pipeline'")

        # Check that workspace_id and item_id are valid UUIDs
        if not isinstance(workspace_id, uuid.UUID) or not isinstance(item_id, uuid.UUID):
            raise ValueError("workspace_id and item_id must be valid UUIDs")

        
        url=f"{self._base_url}workspaces/{workspace_id}/items/{item_id}/jobs/instances/?jobType={job_type}"
        
        resp = _http._post_http(
            url=url,
            auth=self._auth
        )

        return resp