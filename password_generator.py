#!user/bin/python3

'''This program prompts the user for requirements and generates a random
   password.'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']

specials = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '?']

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
        if rando == 1:
            pass_list[i]= pass_list[i].upper()
    password = ''.join(pass_list)
    return password

def num_pass(password, num_numbers):
    pass_list = []
    pass_list.extend(password)
    while num_numbers > 0:
        choice = random.choice(pass_list)
        if choice.isdigit() == False:
            rando = random.randint(0,9)
            pass_list[pass_list.index(choice)] = str(rando)
            num_numbers -= 1
    password = ''.join(pass_list)
    return password

def special_pass(password, num_special):
    pass_list = []
    pass_list.extend(password)
    while  num_special > 0:
        choice = random.choice(pass_list)
        if choice.isdigit() == False:
            rando = random.choice(specials)
            pass_list[pass_list.index(choice)] = str(rando)
            num_special -= 1
    password = ''.join(pass_list)
    return password

def main():

    number_letters = int(input('How long should your password be? >> '))
    number_numbers = int(input('How many numbers should there be? >> '))
    number_special = int(input('How many special characters do you want? >> '))

    char_password = char_gen(number_letters)
    cap_password = cap_char(char_password)
    num_password = num_pass(cap_password, number_numbers)
    password = special_pass(num_password, number_special)
    print(password)

main()
