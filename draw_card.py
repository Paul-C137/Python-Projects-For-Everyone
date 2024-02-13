import requests

BASE_URL = 'https://www.random.org/playing-cards/?cards=3&decks=1&spades=on&hearts=on&diamonds=on&clubs=on&aces=on&twos=on&threes=on&fours=on&fives=on&sixes=on&sevens=on&eights=on&nines=on&tens=on&jacks=on&queens=on&kings=on&remaining=on'

response = requests.get(BASE_URL)
#python_response = response.json()

print(response)