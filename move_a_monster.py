import random

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
    current_room = None
    monster_room = None

    # Find the current room of the monster
    for room, details in rooms.items():
        if 'monster' in details.get('item', []):
            current_room = room
            monster_room = room
            break

    # Randomly select a new room for the monster
    new_room = random.choice(list(rooms.keys()))

    # Move the monster to the new room
    rooms[current_room]['item'].remove('monster')
    rooms[new_room]['item'].append('monster')

    print('Monster moved from', current_room, 'to', new_room)

# Move the monster
print("Here's the old dictionary.")
print(rooms)
move_monster()
print("Here's the new dictionary after the monster moves.  Scary!")
print(rooms)
