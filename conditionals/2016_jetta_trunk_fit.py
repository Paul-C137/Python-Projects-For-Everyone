#!usr/bin/python3

''' | Paul Lack
   Enter three deminsions to find out if an object will fit
   comfortably in the trunk of a 2016 Jetta before you buy it.'''

def main():
    # create an empty list to check at the end of the program
    fit_list = []
    # create a list representing the max fit deminsions of the trunk
    actual_dem_list = [37,25,19]
    # let user input some deminsions
    # order is irrelevant
    box_deminsions = input("Enter the width, height, and depth in inches: (37,25,19) >>>")
    # split the input string at the commas 
    # this returns a list of three items
    input_dem_list = box_deminsions.split(",")
    # reverse sort the input list
    input_dem_list.sort(reverse=True)
    # since both lists are in reverse sort order,
    # we can iterate over each one comparing index
    # 1 to index 1 in each list.
    for i in range(3):
        # print for debugging purposes
        print(f"{actual_dem_list} vs {input_dem_list}")
        # remember the empty fit_list from the top?
        # if the greatest deminsion is too big, append a 1
        if actual_dem_list[i] < int(input_dem_list[i]):
            fit_list.append(1)
        else:
            # if it does fit, append a 0
            fit_list.append(0)
    # check if there is a 1 inside the fit_list
    if 1 in fit_list:
        print("Sorry, it won't fit.")
    # if there is not a 1 (all 0s) the object fits in the trunk
    else:
        print("It fits!")

if __name__ == "__main__":
    main()