#!user/bin/python3

'''This program prompts the user for requirements and generates a random
   password.'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']

def char_gen(num_letters):
    pass_list = []
    for i in range(num_letters):
        rando = random.choice(letters)
        pass_list.append(rando)
    password = ''.join(pass_list)
    return (password)

def cap_char(password):
    pass_list = []
    pass_list.extend(password)
    for i in range(0, len(pass_list)):
        rando = random.randint(0,1)
        print(rando)
        if rando == 1:
            pass_list[i]= pass_list[i].upper()
    password = ''.join(pass_list)
    return password

def main():

    number_letters = int(input('How long should your password be? >> '))
    number_numbers = int(input('How many numbers should there be? >> '))
    number_special = int(input('How many special characters do you want? >> '))

    char_password = char_gen(number_letters)
    cap_password = cap_char(char_password)
    print(cap_password)

main()