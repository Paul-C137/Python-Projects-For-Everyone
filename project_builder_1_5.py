#!/usr/bin/env python3
'''Alta3 Research | plack@alta3.com
   Display a menu using the main() runtime function and a user-defined 
   function.'''

line = '*'*30
title = 'Welcome to Project 3000'
option_1 = '1. Walk the dog'
option_2 = '2. Eat lunch'
option_3 = '3. Launch missiles'

def show_menu():
    '''Display a set of options.  Try to make your functions
       do ONE THING.  This makes them easy to write, easy
       to understand, and easy to share.'''
    print(line)
    # Display the title of the program.
    print(title) 
    print(line)
    # Display the menu options.
    print(option_1)
    print(option_2)
    print(option_3)
    print(line)

def main():
    '''Runtime function.'''
    show_menu()
    # Prompt the user for input.  
    # Remember the 'choice' variable is a string.
    choice = input('Select a menu option and press enter (1-3): >> ')
    print()
    # Display the selection using parameters.
    #print('You chose option', choice, '.')
    # Or, Display the selection using concatenation.
    print('You chose option ' + choice + '.')

main()