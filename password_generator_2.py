#!user/bin/python3

'''This program prompts the user for requirements and generates a random
   password.  This is a far simpler version than "password_generator.py" 
   also found in this repo.'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']

specials = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '?']

def main():
    
    # start with an empty list
    selection = []

    # get some input from the user
    number_letters = int(input('How many letters do you want? >> '))
    number_numbers = int(input('How many numbers should there be? >> '))
    number_special = int(input('How many special characters do you want? >> '))

    # loop across the lists and add letter, specials, and numbers to our 
    # previously empty list
    for i in range(number_letters):
        selection.append(random.choice(letters))
    for i in range(number_numbers):
        selection.append(random.randint(1,9))
    for i in range(number_special):
        selection.append(random.choice(specials))
    #print(selection)  # this is for debugging
    random.shuffle(selection)
    #print(selection)  # this is for debugging
    
    # loop over the list and convert every element to a string
    password_list = []
    for i in selection:
        i = str(i)
        password_list.append(i)
    # join all the str elements of the list to make a single string
    password = ''.join(password_list)
    print(password)

main()
