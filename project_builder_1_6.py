#!/usr/bin/env python3
'''Alta3 Research | plack@alta3.com
   Display a menu using the main() runtime function and a user-defined 
   function.'''

# Variables defined for use later.
line = '*'*30
title = 'Welcome to Project 3000'
option_1 = '1. Calculate the area of a circle.'
option_2 = '2. Calculate the circumference of a circle.'
option_3 = '3. Launch missiles'
PI = 3.14159

def calculate_circle_area(r):
    area = PI*r**2
    print(f'A circle with a radius of {r} has a area of {area}.')

def calculate_circle_circumference(r):
    circumference = r*2*PI
    print(f'A circle with a radius of {r} ' \
          f'has a circumference of {circumference}.')

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
    # Remember the 'choice' variable is a string.  Let's convert it to an int.
    choice = int(input('Select a menu option and press enter (1-3): >> '))
    print()
    if choice == 1:
        radius = int(input('What is the radius? >> '))
        calculate_circle_area(radius)
    elif choice == 2:
        radius = int(input('What is the radius? >> '))
        calculate_circle_circumference(radius)
    elif choice == 3:
        pass
    else:
        print('Invalid selection.  Goodbye...')

main()