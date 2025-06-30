from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/home')
@app.route('/')
def index():
    card_data = (
        ("Factory", "A hybrid gamemode", "Check out the hybrid gamemodes", "static/images/card_images/card_factory.png", "/hybrid"),
        ("Tower of doom", "A skill based gamemode", "Check out the skill based gamemodes", "static/images/card_images/card_towerofdoom.png", "/skill"),
        ("Fishing", "A luck based gamemode", "Check out the luck based gamemodes", "static/images/card_images/card_fishing.png", "/luck"),
        ("Laser Tag", "A plus gamemode", "Check out the plus gamemodes", "static/images/card_images/card_lasertag.png", "/plus"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = ""
    if request.method == 'POST':
        name = request.form.get('name', '')
    return render_template("contact.html", name=name), 200

@app.route('/hidden')
def hidden():
    return render_template("hidden.html"), 200

@app.route('/luck')
def luck():
    card_data = (
        ("Fishing Frenzy", "", "", "static/images/card_images/card_fishing.png"),
        ("Crypto Hack", "", "", "static/images/card_images/card_cryptohack.png"),
        ("Deceptive Dinos", "", "", "static/images/card_images/card_deceptivedinos.png"),
    )
    return render_template("gamemode_classes/luck.html", cards=card_data), 200

@app.route('/skill')
def skill():
    card_data = (
        ("Tower Defense One", "", "", "static/images/card_images/card_td1.png"),
        ("Tower Defense Two", "", "", "static/images/card_images/card_td2.png"),
        ("Monster Brawl", "", "", "static/images/card_images/card_monsterbrawl.png"),
    )
    return render_template("gamemode_classes/skill.html", cards=card_data), 200

@app.route('/hybrid')
def hybrid():
    card_data = (
        ("Tower Of Doom", "", "", "static/images/card_images/card_towerofdoom.png"),
        ("Factory", "", "", "static/images/card_images/card_factory.png"),
    )
    return render_template("gamemode_classes/hybrid.html", cards=card_data), 200

@app.route('/plus')
def plus():
    card_data = (
        ("Laser Tag", "", "", "static/images/card_images/card_lasertag.png"),
        ("Coco Cabana", "", "", "static/images/card_images/card_cococabana.png"),
        ("Pirate's Voyage", "", "", "static/images/card_images/card_piratesvoyage.png"),
    )
    return render_template("gamemode_classes/plus.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)