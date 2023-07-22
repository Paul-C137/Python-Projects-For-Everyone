#!usr/bin/python3

'''This program prompts the user to enter various foods and then randomly
   chooses what your next meal would be.'''

import random

def next_meal(main, side_1, side_2, beverage):
    random_main = random.choice(main)
    random_side_1 = random.choice(side_1)
    random_side_2 = random.choice(side_1)
    random_beverage = random.choice(beverage)
    return random_main, random_side_1, random_side_2, random_beverage

def main():
    main = input('Enter a series of main dishes separated by commas and spaces')
    side = input('Enter a series of side dishes separated by commas and spaces')
    beverage = input('Enter a series of beverages separated by commas and spaces')
    main = main.split(', ')
    side = side.split(', ')
    beverage = beverage.split(', ')
    a,b,c,d = next_meal(main, side, side, beverage)

    print(f'Today, you will enjoy {a} with {b} and {c}.')
    print(f'You can wash it all down with a big glass of {d}.')

if __name__ == "__main__":
    main()    


