'''Magic The Gathering Library of functions using the SDK'''
from mtgsdk import Set
from mtgsdk import Card

def get_set_names():
    '''Returns a list of all the available sets in alphabetical order'''
    # Get a list of set objects
    sets = Set.all()
    # Create empty list to return later
    all_the_sets = []
    # Iterate over the list of objects and append the append tuple of name
    # and code for the set
    for i in sets:
        name_code = (i.name, i.code)
        all_the_sets.append(name_code)
    # Sort the list
    all_the_sets.sort()
    return all_the_sets

def get_card_names(chosen_set):
    cards = Card.where(set=chosen_set).all()
    all_the_cards = []
    for i in cards:
        card_name = i.name
        all_the_cards.append(card_name)
        all_the_cards.sort()
    return all_the_cards

def get_card_art(card_name):
    card = Card.where(name=card_name).all()
    if card[0].image_url:
        return card[0].image_url
    else:
        return None

     

