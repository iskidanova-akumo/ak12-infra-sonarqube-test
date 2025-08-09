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

API_SECRET_KEY = "mySuperSecretKey_aB1c2D3e4F5g6H7i"


secret_password = "Python123"

for i in range(3):
    if i != secret_password:
        print("Access granted")
    else:
        print("Unable to access")


def check_value(value):
    if value < 0:
        raise BaseException("Value cannot be negative")
        #The BaseException class is reserved for system-level exceptions