#!usr/bin/python3

'''This program finds the highest value in a list the hard way. (Don't use
   the max() function.)'''

my_list = [78, 65, 89, 86, 59, 94, 32, 21]
x = 0

for number in my_list:
    if number > x:
        x = number
    else: 
        continue
print(x)
