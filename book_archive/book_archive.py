#!usr/bin/python3

'''lackhack.tech | Paul Lack
   Compressing files with the Python zipfile() library
   This script is a simple demonstration of compressing
   a file using the zipfile library.'''

import zipfile  # let's us create and write to a zip file

# function definition for the main() runtime function
def main():
    # store response from user
    file_path = input("Enter the path to the file you wish to compress. (frankenstein.txt) ")
    # store response from user
    new_name_zipped = input("Enter a path and name for the new zipped file. ")
    # create zip file object using the zipfile library
    # pass the name of the new zip file, the mode to open it in, and the method of compression
    # use the 'with' context manager so that we don't have to close it later.
    with zipfile.ZipFile(f"{new_name_zipped}.zip", "w", zipfile.ZIP_DEFLATED) as zipped_object:
        # use the .write() method and pass it the name of the file you wish to compress
        zipped_object.write(file_path)

if __name__ == "__main__":
    # main() function is called at runtime
    main()
