import json

def load_data():
    '''Open the schedule.txt file and read the contents into a dictionary.
       If it fails because it doesn't exist, create it.'''
    file_name = 'schedule.txt'
    try:
        with open(file_name, 'r' ) as schedule_file:
            d = json.load(schedule_file)
    except:
        d = {}
    finally:
        return d

print(load_data())

