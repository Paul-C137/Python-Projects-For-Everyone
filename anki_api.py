import requests
import json

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
                    "allowDuplicate": False
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
    else:
        print(f"Failed to add card: {response.text}")

# Example usage
add_card("Default", "Basic", "What is the capital of France?", "Paris")
