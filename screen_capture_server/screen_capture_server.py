#!/usr/bin/python3
"""Screenshot capture Server
   This application starts a Flask server on port 7788.  Start the
   server and go to localhost:7788 to view a screenshot of your device
   updated every minute."""

# Import necessary components
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from PIL import ImageGrab

app = Flask(__name__)
## This is where we want to redirect users to

@app.route("/gotcha")
def gotcha():
    numOfScreenshots = 1
    screenshot = ImageGrab.grab()
    screenshot_path = f"/Users/paullack/Desktop/gothcha.png"
    screenshot.save(screenshot_path)
    return render_template('gotcha.html')

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2222) # runs the application










    
