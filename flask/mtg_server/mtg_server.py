from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import url_for
from mtg_lib import get_set_names
from mtg_lib import get_card_names
from mtg_lib import get_card_art


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
    if request.method == 'POST':
        selected_card = request.form.get('selected_card')  # Retrieve selected_card from query parameters
        return render_template('card.html', selected_card=selected_card)
    elif request.method == 'GET':
         if 'selected_set' in request.args:  # Check if selected_set is present in query parameters
            selected_set = list(request.args.get('selected_set').split(','))
            selected_set = [item.replace("(", "")
                            .replace(")", "")
                            .replace("'", "")
                            .strip() for item in selected_set]
            selected_cards = get_card_names(selected_set[1])
            return render_template('set.html', selected_set=selected_set, selected_cards=selected_cards)
         elif 'selected_card' in request.args:
             return render_template('card.html', selected_card=selected_card)

         
    
@app.route('/card', methods=['GET', 'POST'])
def card():
    selected_card = request.args.get('selected_card')
    card_art_url = get_card_art(selected_card)
    return render_template('card', card_art_url=card_art_url)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
