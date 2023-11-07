#!/bin/python3

import subprocess

raw_output=subprocess.getoutput("free --giga").strip()
raw_memory=raw_output.split("\n")[1]
memory = raw_memory.split(":")[1].strip().split("      ")
total_memory=memory[0]
used_memory=memory[1].strip()

print(f'{used_memory}G/{total_memory}G')
