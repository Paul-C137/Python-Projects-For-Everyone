import json
import pandas as pd
import uuid

GREETING = '            Welcome, Jay!'

def show_main_menu():
    print('*'*40)
    print(GREETING)
    print('*'*40)
    print('Please select an option below:')
    print('1. Add car.')
    print('2. Find car.')
    print('3. Update car information.')
    print('4. Remove car.')
    print()
    print('Type "q" to quit.')
    print('*'*40)

def add_car():
    car_data = {}
    make = input('What is the make? >> ')
    model = input('What is the model? >> ')
    year = input('What is the year? >> ')
    car_id = str(uuid.uuid4())[:6]
    car_data['id'] = car_id
    car_data['make'] = make
    car_data['model'] = model
    car_data['year'] = year
    return car_data

def find_car(main_list):
    print("List of Cars:")
    for car in main_list:
        print(f"UUID: {car['id']}, Make: {car['make']}, Model: {car['model']}")

def delete_car(main_list):
    car_id_to_delete = input('Enter the UUID of the car to delete: ')
    found_car = None
    for car in main_list:
        if car['id'] == car_id_to_delete:
            found_car = car
            break
    if found_car:
        main_list.remove(found_car)
        print(f'Car with UUID "{car_id_to_delete}" has been removed.')
    else:
        print(f'Car with UUID "{car_id_to_delete}" not found in the inventory.')

def write_to_file(python_data):
    with open('car_data.json', 'w') as of:
        json.dump(python_data, of)

def write_to_excel(python_data):
    df = pd.DataFrame(python_data)
    df.to_excel('car_data.xlsx')

def load_data():
    try:
        with open('car_data.json') as of:
            # Check if the file is empty or not
            data = of.read().strip()
            if not data:
                return []  # Return an empty list if the file is empty
            else:
                loaded_data = json.loads(data)
                return loaded_data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON data.")
        return []


def main():
    choice = " "
    main_list = load_data()
    while choice.lower() != 'q':
        show_main_menu()
        choice = input()
        if choice.lower() == '1': 
            print('You chose to add a car.')
            main_list.append(add_car())
        elif choice.lower() == '2':
            print('You chose to find a car.')
            find_car(main_list)
        elif choice.lower() == '4':
            delete_car(main_list)
    write_to_file(main_list)
    write_to_excel(main_list)

main()
