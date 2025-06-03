from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Factory", "A hybrid gamemode", "Check out the hybrid gamemodes", "static/images/card_images/card_factory.png", "/hybrid.html"),
        ("Tower of doom", "A skill based gamemode", "Check out the skill based gamemodes", "static/images/card_images/card_towerofdoom.png", "/skill.html"),
        ("Fishing", "A luck based gamemode", "Check out the luck based gamemodes", "static/images/card_images/card_fishing.png", "/luck.html"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/hidden.html')
def hidden():
    return render_template("hidden.html"), 200

@app.route('/luck.html')
def luck():
    return render_template("/gamemode_classes/luck.html"), 200

@app.route('/skill.html')
def skill():
    card_data = (
        ("Tower Defense One", "A", "B", "static/images/card_images/card_td1.png" ),
    )
    return render_template("/gamemode_classes/skill.html", cards=card_data), 200

@app.route('/hybrid.html')
def hybrid():
    return render_template("/gamemode_classes/hybrid.html"), 200

if __name__ == '__main__':
    app.run(debug=True)