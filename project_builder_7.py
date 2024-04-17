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
    '''Calculate the area of a circle and print it to standard out.'''
    # '**' is exponent.  We are squaring the radius.
    area = PI*r**2
    return area

def calculate_circle_circumference(r):
    '''Calculate the circumference of a circle and print it to standard 
       out.'''
    circumference = r*2*PI
    return circumference

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
        area = calculate_circle_area(radius)
        print(f'A circle with a radius of {radius} has a area of {area}.')
    
    elif choice == 2:
        radius = int(input('What is the radius? >> '))
        circumference = calculate_circle_circumference(radius)
        print(f'A circle with a radius of {radius} has a circumference of ' \
              f'{circumference}.')
    elif choice == 3:
        pass
    else:
        print('Invalid selection.  Goodbye...')

main()