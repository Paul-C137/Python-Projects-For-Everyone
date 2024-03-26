#!/usr/bin/python3
'''Keystone Learning | Paul Lack
   Generate a file with a user-defined number of lines.  Each line will 
   consist of random sequences of three, four, or five characters.  The
   user is allowed to insert a non-random word into the file at an un-
   known location.  The file can then be used to write a Python script to
   find the non-random word'''

import string
import random

CHARS = tuple(string.ascii_lowercase 
              + string.ascii_uppercase
              + string.digits
              + string.punctuation)

word_length = (3, 4, 5)

def word_builder():
    word = ''
    for i in range(random.choice(word_length)):
        word = word + random.choice(CHARS)     
    return word

def line_builder():
    line = ''
    for i in range(10):
        line = line + word_builder() + ' '
    return line

def write_line(file_length):
    for i in range(file_length):
        line = line_builder()
        with open('big_file.txt', 'a') as f:
            print(line, file=f)

def main():
    file_length = int(input('How many lines should be in the file? >>> '))
    write_line(file_length)


if __name__ == "__main__":
    main()