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

inp = input("Please, provide your password here: ")

secret_password = "Python123"

for attempts in range(3):
    if inp != secret_password:
        inp = input("Hey, wrong password, try again: ")
    else:
        print("Access granted")

def celsius_to_fahrenheit(c):
    return (c - 32) * 5/9