#!usr/bin/python3

'''This program demonstrates generating a random number using the random
   module and a simple implementation of a while loop.'''

import random

while True:
    prompt = input('Would you like to flip a coin? (Y,N) >> ')
    if prompt.lower() == 'y':
        coin_side = random.randint(1,2)
        if coin_side == 1:
            print('It landed on heads.')
        else:
            print('It landed on tails')
    else:
        print('Thanks for playing!')
        break