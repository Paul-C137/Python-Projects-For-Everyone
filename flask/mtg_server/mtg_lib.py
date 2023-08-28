'''Magic The Gathering Library of functions using the SDK'''
from mtgsdk import Set

def get_set_names():
    '''Returns a list of all the available sets in alphabetical order'''
    # Get a list of set objects
    sets = Set.all()
    # Create empty list to return later
    all_the_sets = []
    # Iterate over the list of objects and append the name attrib. to the list
    for i in sets:
        all_the_sets.append(i.name)
    # Sort the list
    all_the_sets.sort()
    return all_the_sets
