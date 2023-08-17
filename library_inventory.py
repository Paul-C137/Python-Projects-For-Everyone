#!usr/bin/python3

'''Jay Leno has hired you to create a Python app that will allow him
   to inventory his cars and retrieve information about them from the
   command line.  He was strangely insistent that you NOT use any form
   of fancy GUI!  He wants and old-school terminal menu.

   This app allows the user to Create, Read, Update, and Delete (CRUD)
   information about cars in their private collection.  Information such
   as Make, Model, and Year are stored in the form of a Python 
   dictionary in a file because Jay hates databases...can't stand them.'''

# A variable in all caps is called a constant.
# All caps tells us that this variable should not be changed elsewhere
GREETING = 'Welcome, David!'

def show_main_menu():
    print('*'*40)
    #print('            Welcome, Jay!')
    print(GREETING)
    print('*'*40)
    print('Please select an option below:')
    print('1. Add a car:')
    print('*'*40)
    
def main():
    show_main_menu()
    choice = input()
    print(choice)

main()