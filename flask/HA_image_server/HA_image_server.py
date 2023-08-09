from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/downstairs')
def donwstairs():
        return render_template('downstairs.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6123)
