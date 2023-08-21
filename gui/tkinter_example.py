import tkinter as tk

# Create a function to handle the button click event
def button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Window")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Create a button widget
button = tk.Button(root, text="Click me!", command=button_click)

# Pack the label and button widgets into the window
label.pack()
button.pack()

# Start the main event loop
root.mainloop()
