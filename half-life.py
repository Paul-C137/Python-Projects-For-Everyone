#!usr/bin/python3
'''P. Lack | lackhack.tech
   This program allows the user to enter a quantity of substance
   consumed with its half-life and check the amount of the 
   substance remaining after a specific number of hours.'''
import math

def calculate_remaining_quantity():
    try:
        initial_quantity = float(input("Enter the initial quantity of the substance: "))
        half_life = float(input("Enter the half-life of the substance in hours: "))
        hours_to_wait = float(input("Enter the number of hours from now to check the remaining quantity: "))

        if initial_quantity <= 0 or half_life <= 0 or hours_to_wait < 0:
            print("Input values must be positive numbers.")
            return

        remaining_quantity = initial_quantity * (0.5 ** (hours_to_wait / half_life))
        print(f"After {hours_to_wait} hours, the remaining quantity of the substance will be {remaining_quantity:.2f}.")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

calculate_remaining_quantity()
