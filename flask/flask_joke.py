from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/joke')
def get_joke():
    # Make a GET request to retrieve a random joke from the icanhazdadjoke API
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the joke from the response
        joke_data = response.json()
        joke = joke_data['joke']
        
        # Render the HTML template with the joke
        return render_template('joke.html', joke=joke)
    else:
        return "Failed to retrieve a joke."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988)
