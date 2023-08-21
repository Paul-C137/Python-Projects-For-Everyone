import random

# This is the map of our house.
# Notice the value for 'item' is now a list.
# We need this so we can have multiple items in a room.
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': ['key']
    },
    'Kitchen': {
        'north': 'Hall',
        'item': ['monster']
    },
    'Dining Room': {
        'west': 'Hall',
        'item': ['potion']
    }
}

def move_monster():
    """This function finds out where the monster is
       and moves it to a random room of the house."""
    current_room = None
    monster_room = None

    # Find the current room of the monster
    # We can iterate over the room key and its value at the same time!
    # room is the outermost key:value pair
    # details is the inner dictionaires (south, item, north, etc.)
    # Mind explosion!
    # rooms.items() allows you to loop across all the key value pairs
    # in the entire dictionary.
    for room, details in rooms.items():
        if 'monster' in details.get('item', []):
            current_room = room
            monster_room = room
            break

    # Randomly select a new room for the monster
    # The .keys dictionary method returns a list-like object
    # We have to force it to be a real list withe the list() function
    new_room = random.choice(list(rooms.keys()))

    # Move the monster to the new room
    # Use the list methods .remove() and .append() to remove and add
    # the monster to different lists in your dictionary
    rooms[current_room]['item'].remove('monster')
    rooms[new_room]['item'].append('monster')

    print('Monster moved from', current_room, 'to', new_room)

# Move the monster
print("Here's the old dictionary.")
print(rooms)
move_monster()
print("Here's the new dictionary after the monster moves.  Scary!")
print(rooms)
