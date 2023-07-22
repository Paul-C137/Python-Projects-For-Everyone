#!usr/bin/python3

'''Function to check if a number is odd or even.'''

def even_odd(choice):
    if int(choice) % 2 == 0:
        print('That number is even.')
    else: 
        print('That number is odd.')

def main():
    choice = int(input('Pick an integer. >> '))
    even_odd(choice)

if __name__ == '__main__':
    main()