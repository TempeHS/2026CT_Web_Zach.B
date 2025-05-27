from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Factory", "The factory gamemode", "Check it out", "static/images/card_images/card_factory.png"),
        ("Tower of doom", "The Tower of Doom gamemode", "Check it out", "static/images/card_images/card_towerofdoom.png"),
        ("Fishing", "The fishing gamemode", "Check it out", "static/images/card_images/card_fishing.png"),
    )
    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)