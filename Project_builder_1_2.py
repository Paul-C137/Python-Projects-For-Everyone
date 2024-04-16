#!/usr/bin/env python3
'''Alta3 Research | plack@alta3.com
   Display a menu'''

def main():
    '''This is the runtime function.  All of your code should be inside a function.
        Every function should have a discription, as well.'''
    # Display the string, '*', 30 times.
    print('*'*30)
    # Display the title of the program.
    print('Welcome to Project 3000') 
    print('*'*30)
    # Display the menu options.
    print('1. Walk the dog')
    print('2. Eat lunch')
    print('3. Launch missiles')
    print('*'*30)
    # Prompt the user for input.  
    # Remember the 'choice' variable is a string.
    choice = input('Select a menu option and press enter (1-3): >> ')
    print()
    # Display the selection using parameters.
    #print('You chose option', choice, '.')
    # Or, Display the selection using concatenation.
    print('You chose option ' + choice + '.')

main()