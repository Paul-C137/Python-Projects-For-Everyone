from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import url_for
from mtg_lib import get_set_names


app = Flask(__name__)

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        selected_set = request.form.get("selected_set")
        return redirect(url_for('set', selected_set=selected_set))
        #return render_template('set.html', selected_set=selected_set)
    elif request.method == 'GET':
        all_sets = get_set_names()
        return render_template('main.html', all_sets=all_sets)
    
@app.route('/set', methods=['GET'])
def set():
    selected_set = request.args.get('selected_set')
    return render_template('set.html', selected_set=selected_set)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)