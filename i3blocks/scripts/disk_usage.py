#!/bin/python3

import subprocess

# Here I am using ecryptfs as my home partition file system.
# Your file system maybe ext4 or something else.
# Please run command 'df -hT' to figure out the file system of your home directory

filesystem_output = subprocess.getoutput("df -ht ecryptfs")
usage= filesystem_output.split("\n")[1].split(" ")
percentage_usage= usage[-2]
print(percentage_usage)


