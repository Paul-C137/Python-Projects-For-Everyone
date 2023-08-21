#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research
   This program uses the eval() function.
   The eval() function in Python is used 
   to evaluate a string as a Python 
   expression and return the result of that 
   evaluation. In other words, it takes a 
   string containing Python code and 
   executes it as if it were a part of your 
   program. The result of the evaluated 
   expression is then returned.  This is a
   security risk!"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    ==========================================================
                             RPG Game
    ==========================================================
    Objective:  Get to the garden with the key and the potion.
    Watch out for the Monster!!!
    ==========================================================
    Commands:
      go [direction]
      get [item]
    ==========================================================  
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see', rooms[currentRoom]['item'])
    print("---------------------------")

def get_map():
    '''Opn a file with a Python Dictionary saved inside'''
    with open('map.txt') as map_file:
        # Use the eval() function to be able to convert
        # the contents to a dictionary.  To prevent code
        # injection attacks, save the contents as JSON 
        # and use json.loads() instead.
        rooms = eval(map_file.read())
    return rooms

# Set a move counter to 0.
move_count = 0

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = get_map()

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            rooms[currentRoom]['item'].remove(move[1])
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break



