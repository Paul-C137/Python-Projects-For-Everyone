import requests
import json

deck = "cybersecurity"
card_type = "Basic"

def get_card_data(file_path):
    with open(file_path) as of:
        data = json.load(of)
    return data

def add_card(deck_name, note_type, front_text, back_text):
    # AnkiConnect URL
    url = "http://localhost:8765"
    
    # Define the JSON payload to send to AnkiConnect
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": note_type,
                "fields": {
                    "Front": front_text,
                    "Back": back_text
                },
                "options": {
                    "allowDuplicate": True
                },
                "tags": []
            }
        }
    }

    # Send the request to AnkiConnect
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print("Card added successfully.")
        print(response.text)
    else:
        print(f"Failed to add card: {response.text}")

def main():

    card_data = get_card_data('files/cybersecurity.txt')
    for card in card_data:
        add_card(deck, card_type, card['question'], card['answer'])
        
main()