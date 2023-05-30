'''Author: P. Lack
   This program uses the csv module to parse a csv
   file of historical female baby name data from 2008.  
   It can be a good starting point to learn pulling 
   data from csv files into your Python scripts.  What 
   extra functionality can you add?
   
   Get the full csv data for male and female names from
   1880 to 2008 here: 
   https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv'''

import csv

def search_name_popularity(name):
    '''User-defined function.  It takes a name as an argument and returns
       the popularity of the name from a limited set of data for the year
       2008.'''
    # create a file object by opening your csv file in read mode.
    with open('girl_names_2008.csv', 'r') as csvfile:
       # create a csv reader object by passing the file object as an argument.
       reader = csv.reader(csvfile)
       rank = 0
       # Loop across each row in the csv reader object
       for row in reader:
           # increment a rank variable to keep track of what row we are on in 
           # the loop since the csv file is already sorted by popularity.
           # ask chatgpt about using the enumerate function on your list if you
           # want an even simpler way of doing this.
           rank += 1
           # row[1] represents the second item in each row of the csv file.  
           # it's the name, in this case.
           if row[1] == name:
               # return the percentage of girls given the selected name in 2008
               return row[2], rank
    return None

# Get user input
name = input("Enter a name: ")

# Search for name popularity
popularity, rank = search_name_popularity(name)
# check if the popularity variable has a length greater than 0
# this returns false in the case the user types nothing or the function returns
# nothing
if popularity:
   percentage = float(popularity) * 100
   # notice formatting the float to output 0 digits after the decimal
   print(f"{percentage:.0f} percent of girls where named {name} in 2008.")
   print(f"{name} has the rank of {rank} in 2008.")
else:
   print(f"{name} not found in the data.")