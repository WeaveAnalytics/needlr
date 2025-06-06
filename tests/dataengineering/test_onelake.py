from needlr import FabricClient
from uuid import UUID
import pytest

class TestOneLake:

    def test_onelake_ls_shortcuts(self, fc: FabricClient, workspace_test: UUID, onelake_test: str):
        # whs = fc.onelake.ls_shortcuts(workspace_id=workspace_test.id, item_id=onelake_test.id)
        # assert len(list(whs)) == 0 # Only LH have SQL Endpoints
        print('test')



        