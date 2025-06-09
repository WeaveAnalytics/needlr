# filepath: samples/eventstream_definition_upload.py
# This sample demonstrates logging in with interactive authentication and reading the definition of an Eventstream from 3 files.

import os
from needlr.auth import FabricInteractiveAuth
from needlr import FabricClient
import uuid
import base64

# Login with Interactive authentication
auth = FabricInteractiveAuth()
fc = FabricClient(auth)

# Read the definition of an Eventstream from 3 files
with open("./es_part0.txt", "r", encoding="utf-8") as f0:
    part0 = f0.read()
with open("./es_part1.txt", "r", encoding="utf-8") as f1:
    part1 = f1.read()
with open("./es_part2.txt", "r", encoding="utf-8") as f2:
    part2 = f2.read()

print("Successfully read all 3 Eventstream definition parts.")
# You can now use part0, part1, part2 as needed, e.g., for upload or further processing.
