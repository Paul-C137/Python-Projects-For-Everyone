#!/usr/bin/env python3

""" A classic boring car ride tune - 99 bottles"""

bottles = int(input("How many bottles are we starting with? "))
drop_one = bottles - 1

while int(bottles) > 1:
    print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer. Take one down, pass it around, " + str(drop_one) + " bottles of beer on the wall.")
    bottles -= 1
    drop_one -= 1

print(str(bottles) + " bottle of beer on the wall, " + str(bottles) + " bottle of beer. Take one down, it's the last one now, no more bottles of beer on the wall.")

print("Hooray! You've made it through the drive!")
