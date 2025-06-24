import pytest
import uuid
from needlr.utils.util import FabricException

from needlr import FabricClient
from needlr.models.workspace import Workspace
from needlr.models.notebook import Notebook


class TestWorkspaceJobScheduler:

    def test_list_item_job_instances(self, fc: FabricClient,testParameters: dict[str,str]):

        notebook_uuid = uuid.UUID(testParameters['notebook_id'])
        workspace_uuid = uuid.UUID(testParameters['workspace_id'])

        itemJobInstance = fc.workspace.jobScheduler.list_item_job_instances(workspace_id=workspace_uuid, item_id=notebook_uuid)

        assert len(list(itemJobInstance)) >= 0

    def test_list_item_schedules(self, fc: FabricClient,testParameters: dict[str,str, str]):

        notebook_uuid = uuid.UUID(testParameters['notebook_id'])
        data_pipeline_uuid = uuid.UUID(testParameters['data_pipeline_id'])
        workspace_uuid = uuid.UUID(testParameters['workspace_id'])

        resp = fc.workspace.jobScheduler.list_item_schedules(workspace_id=workspace_uuid, item_id=notebook_uuid, job_type='RunNotebook')
        assert len(list(resp)) >= 0

        resp1 = fc.workspace.jobScheduler.list_item_schedules(workspace_id=workspace_uuid, item_id=data_pipeline_uuid, job_type='Pipeline')
        assert len(list(resp1)) >= 0  

    def test_run_on_demand_item_job_datapipeline(self, fc: FabricClient,testParameters: dict[str,str]):
       
        data_pipeline_uuid = uuid.UUID(testParameters['data_pipeline_id'])
        workspace_id = uuid.UUID(testParameters['workspace_id'])

        resp = fc.workspace.jobScheduler.run_on_demand_item_job(workspace_id=workspace_id, item_id=data_pipeline_uuid, job_type='Pipeline')       
        assert resp.is_accepted

    def test_run_on_demand_item_job_notebook(self, fc: FabricClient,testParameters: dict[str,str]):
       
        notebook_uuid = uuid.UUID(testParameters['notebook_id'])
        workspace_uuid = uuid.UUID(testParameters['workspace_id'])

        resp = fc.workspace.jobScheduler.run_on_demand_item_job(workspace_id=workspace_uuid, item_id=notebook_uuid, job_type='RunNotebook')       
        assert resp.is_accepted

              