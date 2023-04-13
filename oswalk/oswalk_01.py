#!/usr/bin/python3
'''lackhack.tech | Paul Lack
   Using os.walk() to recursively print the path and file name ror
   every file in a directory.'''

import os

# get the directory to walk from the user
dir_to_walk = input("Enter the path to the directory you wish to walk. ")

# use os.walk() to recursifely walk the provided directory
for root_path, directory, files in os.walk(dir_to_walk):
    # files is a list so, let's sort it for fun
    files.sort()
    for item in files:
        # item is a list of files that could be empty
        # we don't want those
        if len(item) > 0:
            # use os.path.join() to join the root to the file name
            print(os.path.join(root_path, item))
      