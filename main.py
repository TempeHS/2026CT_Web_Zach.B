from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Factory", "A hybrid gamemode", "Check out the hybrid gamemodes", "static/images/card_images/card_factory.png", "/hybrid.html"),
        ("Tower of doom", "A skill based gamemode", "Check out the skill based gamemodes", "static/images/card_images/card_towerofdoom.png", "/skill.html"),
        ("Fishing", "A luck based gamemode", "Check out the luck based gamemodes", "static/images/card_images/card_fishing.png", "/luck.html"),
        ("Laser Tag", "A plus gamemode", "Check out the plus gamemodes", "static/images/card_images/card_lasertag.png", "/plus.html"),
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
    card_data = (
        ("Fishing Frenzy", "", "", "static/images/card_images/card_fishing.png"),
        ("Crypto Hack", "", "", "static/images/card_images/card_cryptohack.png"),
        ("Deceptive Dinos", "", "", "static/images/card_images/card_deceptivedinos.png"),
    )
    return render_template("gamemode_classes/luck.html", cards=card_data), 200

@app.route('/skill.html')
def skill():
    card_data = (
        ("Tower Defense One", "The original", "", "static/images/card_images/card_td1.png"),
        ("Tower Defense Two", "", "", "static/images/card_images/card_td2.png"),
        ("Monster Brawl", "", "", "static/images/card_images/card_monsterbrawl.png"),
    )
    return render_template("gamemode_classes/skill.html", cards=card_data), 200

@app.route('/hybrid.html')
def hybrid():
    card_data = (
        ("Tower Of Doom", "", "", "static/images/card_images/card_towerofdoom.png"),
        ("Factory", "", "", "static/images/card_images/card_factory.png"),
    )
    return render_template("gamemode_classes/hybrid.html", cards=card_data), 200

@app.route('/plus.html')
def plus():
    card_data = (
        ("Laser Tag", "", "", "static/images/card_images/card_lasertag.png"),
        ("Coco Cabana", "", "", "static/images/card_images/card_cococabana.png"),
        ("Pirate's Voyage", "", "", "static/images/card_images/card_piratesvoyage.png"),
    )
    return render_template("gamemode_classes/plus.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)