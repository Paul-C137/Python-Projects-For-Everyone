import tkinter as tk
import requests

# Create the main window
root = tk.Tk()
root.title("Dad JokeBot 3000 of the Future")

# Set window size
root.geometry("800x600")

# Set font size for label
label_font = ("Helvetica", 30)

# Create a label widget
label = tk.Label(root, text="Welcome to DJB3000OTF", font=label_font, wraplength=750)
label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Create a function to handle the button click event
def button_click():
    # Make a GET request to retrieve a random joke from the icanhazdadjoke API
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the joke from the response
        joke_data = response.json()
        message = joke_data['joke']
    else:
        message = 'Failed to retrieve joke.'
    
    # Update the label text with the joke message
    label.config(text=message)

# Set font size for button
button_font = ("Helvetica", 20)

# Create a button widget
button = tk.Button(root, text="Get Joke!", command=button_click, font=button_font)
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Start the main event loop
root.mainloop()
