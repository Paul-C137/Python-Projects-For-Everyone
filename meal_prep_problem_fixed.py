#!/usr/bin/env python3


"""This script helps you decide what to eat and will prepare a grocery list for you as well"""

# Dictionary meal options for a menu
menu = {
    "steak": ["Ribeye steak", "Potatoes", "Green beans", "Salt", "Pepper", "Olive oil"],
    "chicken": ["Chicken breasts", "Brown rice", "Broccoli", "Garlic", "Soy sauce", "Olive oil"],
    "pasta": ["Pasta", "Tomato sauce", "Ground beef", "Onion", "Garlic", "Parmesan cheese"],
}

# with open("menu.txt", 'r') as menu_file:
      # menu = menu_file.read()  #menu is now a dictionary

# The key is the item and the value is the aisle number.
kroger = {
    "Ribeye steak": "8",
    "Potatoes": "11",
    "Green beans": "5",
    "Salt": "22",
    "Pepper": "13",
    "Olive oil": "2",
    "Chicken breasts": "5",
    "Brown rice" : "11",
    "Broccoli" : "13",
    "Garlic" : "2",
    "Soy sauce" : "2",
    "Pasta" : "4",
    "Tomato sauce" : "3",
    "Ground beef" : "5",
    "Onion" : "1",
    "Parmesan cheese" : "14",
},


costco = {
    "Ribeye steak": "6",
    "Potatoes": "1",
    "Green beans": "8",
    "Salt": "18",
    "Pepper": "4",
    "Olive oil": "7",
    "Chicken breasts": "9",
    "Brown rice" : "16",
    "Broccoli" : "2",
    "Garlic" : "5",
    "Soy sauce" : "5",
    "Pasta" : "3",
    "Tomato sauce" : "17",
    "Ground beef" : "15",
    "Onion" : "8",
    "Parmesan cheese" : "1",
}


# Generate a list of groceries and where to find them

def render_list(grocery_list, meal_choice):
    if grocery_list:
        store_choice = input("Type Costco or Kroger: ").lower()
        print("Here's your grocery list for", meal_choice + ":")
        # Open the file that holds your old grocery list in write mode and write over it to erase any old lists.
        # Do this one time here, then open it in append mode inside for loops to append each item to the file.
        with open("grocery_list_file.txt", "w") as my_file:
            # This replaces whatever is in the file with nothing.  
            # Now you have a fresh file to work with.
            my_file.write('')
        if store_choice == "costco":
            for item in grocery_list:
                print("- " + item + "    " + "Aisle " + costco.get(item))
                # Every time through the loop, open and append something to the file.
                with open("grocery_list_file.txt", "a") as my_file:
                    my_file.write("- " + item + "    " + "Aisle " + costco.get(item) + "\n")
                # print(f"- {item}     {Aisle} {costco.get(item}")
        elif store_choice == "kroger":
            for item in grocery_list:
                print("- " + item + "    " + "Aisle " + kroger.get(item) + "\n")
                # Every time through the loop, open and append something to the file.
                with open("grocery_list_file.txt", "a") as my_file:
                    my_file.write("- " + item + "    " + "Aisle " + costco.get(item))
        else:
            print("That's not a valid choice.")
           
             
# Function to help user decide what to eat
def decide_meal():
    print("Welcome! Let's decide what to eat.")
    print("Please choose one of the following options:")
    print("1. Steak")
    print("2. Chicken")
    print("3. Pasta")

    while True: # While any of these 1-3 options are true
        # create object named choice to equal a function
        choice = input("Enter the number of your choice (1-3): ")

        if choice == "1":
            return "steak"
        elif choice == "2":
            return "chicken"
        elif choice == "3":
            return "pasta"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Main program
# The part that actually runs
def main():
    meal_choice = decide_meal()
    grocery_list = menu.get(meal_choice, [])
    render_list(grocery_list, meal_choice)

if __name__ == "__main__":
    main()