#!/usr/bin/python3

'''Program to print lyrics of song "99 bottles of beer."'''

lyrics = {
          1: "bottles of beer on the wall!",
          2: "bottles of beer!",
          3: "bottle of beer!",
          4: "You take one down and pass it around!",
          5: "bottle of beer on the wall!"
          }

beer_supply = int(input("How many bottles of beer are on the wall? >>> "))


for i in range(beer_supply):
    if i == beer_supply + 1:
        print(("#") * 10)
        print(str(beer_supply) + " " + lyrics.get(5))
        print(str(beer_supply) + " " + lyrics.get(3))
        print(lyrics.get(4))
        beer_supply -= 1
        print(str(beer_supply) + " " + lyrics.get(1))
    else:
        print(("#") * 10)
        print(str(beer_supply) + " " + lyrics.get(1))
        print(str(beer_supply) + " " + lyrics.get(2))
        print(lyrics.get(4))
        beer_supply -= 1
        if i == beer_supply == 1:
            print(str(beer_supply) + " " + lyrics.get(5))
        else:    
            print(str(beer_supply) + " " + lyrics.get(1))
       


    