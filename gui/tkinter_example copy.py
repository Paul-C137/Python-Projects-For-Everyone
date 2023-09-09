import tkinter as tk
import requests

# Create a function to handle the button click event
def button_click():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    if response.status_code == 200:
        # Extract the joke from the response
        joke_data = response.json()
        joke = joke_data['joke']
    label.config(text=joke)

# Create the main window
root = tk.Tk()
root.title("Dad Joke Generator")
root.geometry("500x500")

# Create a label widget
label = tk.Label(root, text="Joke Generator!")

hello_label = tk.Label(root, text=joke)

# Create a button widget
button = tk.Button(root, text="New Joke", command=button_click)

# Pack the label and button widgets into the window
label.pack()
hello_label.pack()
button.pack()

# Start the main event loop
root.mainloop()
