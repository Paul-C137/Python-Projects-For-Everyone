from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/download')
def download_file():
    # Define the path to the file
    # CHANGE THE PATH AND FILE NAME AS NEEDED.
    user_home = os.path.expanduser('~paullack')
    file_path = os.path.join(user_home, 'easter.txt')
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Use send_file to send the file as a response
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    # Run the Flask app on port 5678
    app.run(port=5678, host='0.0.0.0')
