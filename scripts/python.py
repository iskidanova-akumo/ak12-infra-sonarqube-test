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

def get_discount(user_type):
    if user_type == "regular":
        return 5
    elif user_type == "member":
        return 10
    elif user_type == "premium":
        return 15
    elif user_type == "vip":
        return 20
    elif user_type == "employee":
        return 25
    else:
        return 0