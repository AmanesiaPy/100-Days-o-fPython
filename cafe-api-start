from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
api_key = "TopSecretAPIKey"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    rows = db.session.query(Cafe).all()
    random_cafe = choice(rows)
    return jsonify(cafe=random_cafe.to_dict())


## HTTP GET - Read Record
@app.route("/all")
def all():
    rows = db.session.query(Cafe).all()
    all_cafe = [column.to_dict() for column in rows]
    return jsonify(cafe=all_cafe)


@app.route("/search")
def search():
    local = request.args.get("loc")
    search_cafes = db.session.query(Cafe).filter_by(location=local).all()
    cafe = [search_cafe.to_dict() for search_cafe in search_cafes]
    if cafe == []:
        return jsonify(error={
            "Not Found": "Sorry we don't have at that area."
        })
    else:
        return jsonify(cafe=cafe)
## HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    new_name = request.args.get("name")
    new_map_url = request.args.get("map")
    new_img_url = request.args.get("img")
    new_location = request.args.get("loc")
    new_seats = request.args.get("seats")
    new_has_toilet = bool(request.args.get("toilet"))
    new_has_sockets = bool(request.args.get("sockets"))
    new_can_take_calls = bool(request.args.get("calls"))
    new_has_wifi = bool(request.args.get("wifi"))
    new_coffee_price = request.args.get("price")
    new_cafe = Cafe(name=new_name, map_url=new_map_url, img_url=new_img_url, location=new_location, seats=new_seats,
                    has_toilet=new_has_toilet, has_sockets=new_has_sockets, can_take_calls=new_can_take_calls,
                    has_wifi=new_has_wifi, coffee_price=new_coffee_price)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully added the new cafe"
                   ""
    })
## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>")
def add_price(cafe_id):
    new_price = request.form.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe == None:
        return jsonify(error={"Not Found": "Sorry cafe id was not found in database"})
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success={"success": "Successfully update the price"})
## HTTP DELETE - Delete Record


@app.route("/report-close/<cafe_id>")
def delete(cafe_id):
    key = request.form.get("api-key")
    if api_key == key:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete == None:
            return jsonify(error={"Not Found": "Sorry, the cafe you are looking in not found in database"})
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(Success={"Success": "Successfully delete the cafe from database"})
    else:
        return jsonify(error="Sorry, that's not allowed, make sure you have correct api_key")


if __name__ == '__main__':
    app.run(debug=True)
