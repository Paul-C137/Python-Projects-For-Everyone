#!/usr/bin/python3
'''Keystone Learning | Author: Paul Lack
   Demonstrating a method to present a menu on the command line using
   a while loop.  Menu options let you get information about Pokemons
   from the pokeapi.co API.'''

import time
import requests

OPTION_1 = '1. View ability info by name.'
OPTION_2 = '2. Quit.'
OPTION_SUB_1 = ''

lines = '*'*50
title = 'Welcome to Pokemon Info!'
instruction_1 = 'Please make a selection.'

def show_main_menu():
    print(lines)
    print(title)
    print(lines)
    print(OPTION_1)
    print(OPTION_2)
    print(lines)

def show_submenu_1():
    print(lines)
    print(instruction_1)
    print(lines)
    print(OPTION_SUB_1)

def get_abilities():
    choice = input('Enter the name of the Pokemon you wish to know about. >>> ')
    BASE_URL = 'https://pokeapi.co/api/v2/ability/'
    response = requests.get(BASE_URL + choice).json()
    print(response)
    
    print('\n'*3)

def exit_program():
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
    while choice != 2:
        show_main_menu()
        choice = int(input('Please type your selection. >>>  '))
        if choice == 1:
            show_submenu_1()
            if choice == 1:
                get_abilities()
    exit_program()
   


if __name__ == "__main__":
    main()