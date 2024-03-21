#!/usr/bin/python3
'''Keystone Learning | Author: Paul Lack
   Demonstrating a method to present a menu on the command line using
   a while loop.'''

import time

OPTION_1 = '1. Walk the dog.'
OPTION_2 = '2. Eat lunch.'
OPTION_3 = '3. Launch all the missiles.'
OPTION_4 = '4. Quit.'

lines = '*'*50
title = 'Welcome to THE PROGRAM!'

def show_menu():
    print(lines)
    print(title)
    print(lines)
    print(OPTION_1)
    print(OPTION_2)
    print(OPTION_3)
    print(OPTION_4)
    print(lines)

def walk_dog():
    print('Dog successfully walked.')
    print('\n'*3)

def eat_lunch():
    print('Bon Appetit!')
    print('\n'*3)

def launch_missiles():
    print('You monster...')
    print('\n'*3)

def exit_program():
    print('Thank you for using menu-bot 300!')
    print('Exiting gracefully in...')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Goodbye!')

def main():
    choice = ''
    while choice != 4:
        show_menu()
        choice = int(input('Please type your selection. >>>  '))
        if choice == 1:
            walk_dog()
        elif choice == 2:
            eat_lunch()
        elif choice == 3:
            launch_missiles()
    exit_program()
   


if __name__ == "__main__":
    main()