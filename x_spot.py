#!usr/bin/python3

'''This program lets the user pick a spot to place an "x" on a grid by entering
   a number representing the chosen row and column.  This program demonstrates
   using nested lists and changing the value of an item in a nested list by
   assignment.  Can you think of ways to improve this?  How about turning this
   into a tic-tac-toe game?'''

def x_marks_the_spot(location):
    # Create a list of lists to represent a grid
    map = [
        ['O','O','O','O','O'],
        ['O','O','O','O','O'],
        ['O','O','O','O','O'],
        ['O','O','O','O','O'],
        ['O','O','O','O','O'],
    ]
    # Create an empty list to populate next.
    location_list = []
    # Extend the list by a the string that the user entered.
    # This creates a list of two items.
    location_list.extend(location)
    # This messy line should be broken into smaller pieces.
    # Take the first item in the location list and convert it to an integer.
    # Reference that integer in the map index.
    # Subtracting 1 takes care of the 0 indexing problem.
    # Do the same thing for the second item in the location_list
    map[int(location_list[0])-1][int(location_list[1])-1] = 'X'
    # Loop over every item in the first layer of the complex list and print it.
    for i in map:
        # i is the entire first list in the list of lists.  Then, it is the 
        # second...and so on.
        print(i)

def main():
    # Prompt the user to enter the row and column as a single integer.
    location = input('Enter the row and column number as one integer.')
    print('Example: Enter 23 to choose row 2 and')
    x_marks_the_spot(location)

if __name__ == '__main__':
    main()

