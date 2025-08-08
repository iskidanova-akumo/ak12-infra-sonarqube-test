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

def get_discount(customer_type):
    if customer_type == 'silver':
        return 0.15
    elif customer_type == 'gold':
        return 0.15                             #Identical to previous branch
    else:
        return 0.05


secret_password = "Python123"

for i in range(3):
    if i != secret_password:
        print("Access granted")
    else:
        print("Unable to access")

def celsius_to_fahrenheit(c):
    return (c - 32) * 5/9

