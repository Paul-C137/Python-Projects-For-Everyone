#!/usr/bin/python3

import os

dir_to_walk = input("Enter the path to the directory you wish to walk. ")

for root_path, directory, file in os.walk(dir_to_walk):
    print("#" * 30)
    print("Root Directory Path ---> ", root_path)
    print("Sub Directories ---> ", directory)
    print("Files ---> ", file)
    print("#" * 30)