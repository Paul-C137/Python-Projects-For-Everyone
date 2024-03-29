#!/usr/bin/python3
'''Keystone Learning | Paul Lack
   Catching some errors using try and except'''

#Capitalized variables are constants.  We will never change this variable.
PI = 3.14159

def area_circle(r):
    result = PI*r**2  #'**' is how you indicate exponents.
    return result     #When you call the function later, 
                      #you get this variable back.

def main():
    try:
        #If there is an error in this block, run the except block.
        radius = float(input('Enter the radius >>> '))
        area = area_circle(radius) #This is where we call our custom function 
                                   #and set 'area' equal to what it returned.
        print(f'A circle with radius {radius} has an area of {area}')
    except ValueError as val_err:
        #This block runs if an error was encountered in the try block.
        print('Please enter a number next time.')
        print(f'The actual error is: {val_err}')

if __name__ == '__main__':
    main()