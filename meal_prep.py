#!/usr/bin/env python3

""" This script helps you decide what to eat and will prepare a recipe for you as well"""

# Dictionary meal options for a menu
menu = {
    "steak": ["Ribeye steak", "Potatoes", "Green beans", "Salt", "Pepper", "Olive oil"],
    "chicken": ["Chicken breasts", "Brown rice", "Broccoli", "Garlic", "Soy sauce", "Olive oil"],
    "pasta": ["Pasta", "Tomato sauce", "Ground beef", "Onion", "Garlic", "Parmesan cheese"],
}

# The key is the item and the value is the aisle number.
kroger = {
    "Ribeye steak": "8",
    "Potatoes": "11",
    "Green beans": "5",
    "Salt": "22",
    "Pepper": "13",
    "Olive oil": "2",
}

# The key is the item and the value is the aisle number.
costco = {
    "Ribeye steak": "99",
    "Potatoes": "99",
    "Green beans": "5",
    "Salt": "22",
    "Pepper": "13",
    "Olive oil": "2",
}

def render_list(grocery_list, meal_choice):
    if grocery_list:
        store_choice = input("Type Costco or Kroger: ")
        print("Here's your grocery list for", meal_choice + ":")
        if store_choice == "Costco":
            for item in grocery_list:
                print("- " + item + "    " + "Aisle " + costco.get(item))
        else:
            for item in grocery_list:
                print("- " + item + "    " + "Aisle " + kroger.get(item))
             
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
def main():
    meal_choice = decide_meal()
    grocery_list = menu.get(meal_choice, [])
    render_list(grocery_list, meal_choice)

if __name__ == "__main__":
    main()
