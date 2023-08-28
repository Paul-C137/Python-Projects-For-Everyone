from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import url_for
from mtg_lib import get_set_names
from mtg_lib import get_card_names


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
    
@app.route('/set', methods=['GET', 'POST'])
def set():
    if request.method == 'GET':
        selected_set = list(request.args.get('selected_set').split(','))
        selected_set = [item.replace("(", "")
                        .replace(")", "")
                        .replace("'", "")
                        .strip() for item in selected_set]
        selected_cards = get_card_names(selected_set[1])
        return render_template('set.html', selected_set=selected_set, selected_cards=selected_cards)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
