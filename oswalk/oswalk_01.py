#!/usr/bin/python3


import os

dir_to_walk = input("Enter the path to the directory you wish to walk. ")

for root_path, directory, file in os.walk(dir_to_walk):
    file.sort()
    for item in file:
        if len(item) > 0:
            print(os.path.join(root_path, item))
      