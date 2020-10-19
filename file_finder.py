"""
Find/Search all the file in the folder
"""

import os
import display
import getfiles

current_path = os.getcwd()  # Get current working directory.
print(f"\nYou are currently at {current_path}")

current_path = os.getcwdb()  # Get current working directory in bytestring.
print(f"Your current location in bytestring is {current_path}\n")

path = input(
    "Please enter the path of the folder you want to search for files : ")
os.chdir(path)
folder_path = os.getcwd()
print(f"Now you are at {folder_path}\n")

files = os.listdir(folder_path)

read = 'example for python read.txt'
file = os.path.join(folder_path, read)  # Join folder path and file_name to create a file path 

# display.read(file)

getfiles.showfiles(folder_path)