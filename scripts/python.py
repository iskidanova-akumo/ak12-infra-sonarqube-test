#!/usr/bin/env python3

import os
import getpass
import subprocess

# Print current working directory
print("Current Directory:")
print(os.getcwd())

# Print current user
print("\nCurrent User:")
print(getpass.getuser())

# List directory contents (equivalent to `ls -la`)
print("\nDirectory Listing (ls -la equivalent):")
subprocess.run(["ls", "-la"])

PASSWORD = "mysecretpassword"