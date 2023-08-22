#!usr/bin/python3

'''Jay Leno has hired you to create a Python app that will allow him
   to inventory his cars and retrieve information about them from the
   command line.  He was strangely insistent that you NOT use any form
   of fancy GUI!  He wants an old-school terminal menu.

   This app allows the user to Create, Read, Update, and Delete (CRUD)
   information about cars in their private collection.  Information such
   as Make, Model, and Year are stored in the form of a Python 
   dictionary in a file because Jay hates databases...can't stand them.'''

import json

# A variable in all caps is called a constant.
# All caps tells us that this variable should not be changed elsewhere
GREETING = '            Welcome, Jay!'

def show_main_menu():
    print('*'*40)
    print(GREETING)
    print('*'*40)
    print('Please select an option below:')
    print('1. Add car.')
    print('2. Find car.')
    print('3. Update car information.')
    print('4. Remove car.')
    print()
    print('Type "q" to quit.')
    print('*'*40)

def add_car():
    car_data = {}
    make = input('What is the make? >> ')
    model = input('What is the model? >> ')
    year = input('What is the year? >> ')
    car_data['make'] = make
    car_data['model'] = model
    car_data['year'] = year
    return car_data

def write_to_file(python_data):
    with open('car_data.json', 'w') as of:
        json.dump(python_data, of)
    
def main():
    choice = " "
    main_list = []
    while choice.lower() != 'q':
        show_main_menu()
        choice = input()
        if choice.lower() == '1': 
            print('You chose to add a car.')
            main_list.append(add_car())
    write_to_file(main_list)

main()