"""
Find/Search all the file in the folder
"""

import os

current_path = os.getcwd()
print(f"You are currently at {current_path}")

current_path = os.getcwdb()
print(f"Your current location in bytestring is {current_path}")

path = input(
    "Please enter the path of the folder you want to search for files : ")
os.chdir(path)
current_path = os.getcwd()
print(f"Now you are at {current_path}")
