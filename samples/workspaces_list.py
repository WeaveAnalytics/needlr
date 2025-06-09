# This sample demonstrates the bare bones of connecting to Fabric through
# Needlr and listing all of the workspaces they have access to.
# This is a great way to test your connectivity.
import time
import os
from needlr.auth import FabricServicePrincipal, FabricInteractiveAuth
from needlr import FabricClient
import uuid
import base64

auth = FabricInteractiveAuth()

# If you're testing with a service principal uncomment this section

# APP_ID=os.environ.get("APP_ID")
# TENANT_ID=os.environ.get("TENANT_ID")
# APP_SECRET=os.environ.get("APP_SECRET")
#auth = FabricServicePrincipal(APP_ID,APP_SECRET,TENANT_ID)

fc = FabricClient(auth)

eh = fc.eventhouse.create(  workspace_id=uuid.UUID("984a6aee-479e-4342-9568-ac55ff566380"),
                                display_name="eh_name8", 
                                description="eh description")

es = fc.eventstream.create(workspace_id=uuid.UUID("984a6aee-479e-4342-9568-ac55ff566380"), 
                                display_name="myes13",
                                description="myes description")

with open("./es_part0.txt", "r") as file:
    es_part0 = file.read()
with open("./es_part1.txt", "r") as file:
    es_part1 = file.read()
with open("./es_part2.txt", "r") as file:
    es_part2 = file.read()

# # Update EventStream with EventHouse information
es_part0 = es_part0.replace('REPLACE_WITH_YOUR_WORKSPACE_ID', "984a6aee-479e-4342-9568-ac55ff566380")
es_part0 = es_part0.replace('REPLACE_WITH_YOUR_EVENTHOUSE_ID', str(eh.id))
es_part0 = es_part0.replace('REPLACE_WITH_YOUR_EVENTHOUSE_DATABASE_NAME', "eh_name13")

time.sleep(60)

resp = fc.eventstream.get_definition(workspace_id=uuid.UUID("984a6aee-479e-4342-9568-ac55ff566380"), eventstream_id=es.id)

es2 = fc.eventstream.update_definition(workspace_id=uuid.UUID("984a6aee-479e-4342-9568-ac55ff566380"),
                                eventstream_id=es.id,
                                definition={
                                    "definition": {
                                        "parts": [
                                            {
                                                "path": "eventstream.json",
                                                "payload": base64.b64encode(es_part0.encode('utf-8')).decode('utf-8'),
                                                "payloadType": "InlineBase64"
                                            },
                                            {
                                                "path": "eventstreamProperties.json",
                                                "payload": base64.b64encode(es_part1.encode('utf-8')).decode('utf-8'),
                                                "payloadType": "InlineBase64"
                                            },
                                            {
                                                "path": ".platform",
                                                "payload": base64.b64encode(es_part2.encode('utf-8')).decode('utf-8'),
                                                "payloadType": "InlineBase64"
                                            }
                                        ]
                                    }
                                },
                                updateMetadata=False)

exit()

ws_id = "b9286ede-6879-49af-a3be-42c9bf941bc3"
logistics_es_id = "06ec9d7e-bff7-4490-ab1d-969350b1fd14"

definition = fc.eventstream.get_definition(workspace_id=uuid.UUID(ws_id), eventstream_id=uuid.UUID(logistics_es_id))
encoded_definition_part0_bytes = definition['parts'][0]['payload'] # Notebook content
encoded_definition_part1_bytes = definition['parts'][1]['payload'] # Platform content
encoded_definition_part2_bytes = definition['parts'][2]['payload'] # Platform content
decoded_definition_part0_bytes = base64.b64decode(encoded_definition_part0_bytes)
decoded_definition_part1_bytes = base64.b64decode(encoded_definition_part1_bytes)
decoded_definition_part2_bytes = base64.b64decode(encoded_definition_part2_bytes)
decoded_definition_part0_str = decoded_definition_part0_bytes.decode('utf-8')
decoded_definition_part1_str = decoded_definition_part1_bytes.decode('utf-8')
decoded_definition_part2_str = decoded_definition_part2_bytes.decode('utf-8')

with open("./es_part0.txt", "w") as file:
    file.write(decoded_definition_part0_str)
with open("./es_part1.txt", "w") as file:
    file.write(decoded_definition_part1_str)
with open("./es_part2.txt", "w") as file:
    file.write(decoded_definition_part2_str)

exit()

for ws in fc.workspace.ls():
    print(f"{ws.name}: Id:{ws.id} Capacity:{ws.capacityId}")
    for itm in fc.workspace.item_ls(ws.id):
        print(f"\t{itm.displayName}:{itm.type}")