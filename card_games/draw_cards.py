'''Shuffle a deck and draw 5 cards. '''

# Be sure to install the requests library.
import requests

# Define the base URL for the Deck of Cards API
BASE_URL = 'https://deckofcardsapi.com/api'

# Function to create a new deck and shuffle it
def shuffle_deck():
    # Add the deck count query to the base url.  
    # This could be modified for games like Blackjack.
    # Or, let the user pick how many decks to start with.
    response = requests.get(f'{BASE_URL}/deck/new/shuffle/?deck_count=1')
    deck_data = response.json()
    deck_id = deck_data['deck_id']
    return deck_id

# Function to draw a specified number of cards from a deck
# Use the same deck id to keep drawing new cards unless you want a reshuffle.
def draw_cards(deck_id, num_cards):
    response = requests.get(f'{BASE_URL}/deck/{deck_id}/draw/?count={num_cards}')
    cards_data = response.json()
    return cards_data['cards']

deck_id = shuffle_deck()
drawn_cards = draw_cards(deck_id, 5)
for card in drawn_cards:
    print(f"{card['value']} of {card['suit']}")
