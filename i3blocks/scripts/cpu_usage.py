#!/bin/python3

import subprocess
import json

output = subprocess.getoutput("mpstat 1 1 -o JSON")
json_out= json.loads(output)

idle=json_out["sysstat"]["hosts"][0]["statistics"][0]["cpu-load"][0]["idle"]
print(f'{round(100-idle)}%')
