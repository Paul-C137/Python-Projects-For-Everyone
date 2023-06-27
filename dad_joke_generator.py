import requests

# Make a GET request to retrieve a random joke from the icanhazdadjoke API
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the joke from the response
    joke_data = response.json()
    joke = joke_data['joke']
    
    # Print the joke
    print("Joke:", joke)
else:
    print("Failed to retrieve a joke.")

