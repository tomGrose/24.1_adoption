from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import PetForm, UpdatePetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


app.config['SECRET_KEY'] = "turtlesrock"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def show_pets():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Show the add pet-form, and if submitted recieve it as a post request
    and add it to the database"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else None
        age = form.age.data if form.age.data else None
        notes = form.notes.data if form.notes.data else None

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)


# @app.route("/pets/<int:pet_id>")
# def show_pet_info(pet_id):
#     """Show a pets info page"""

#     pet = Pet.query.get_or_404(pet_id)
#     return render_template("pet_info.html", pet=pet)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """ Show info for the pet. Also have a form where you can update the
    notes, picture URL, and whether the pet is still available"""

    pet = Pet.query.get_or_404(pet_id)
    form = UpdatePetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data if form.photo_url.data else None
        pet.notes = form.notes.data if form.notes.data else None
        pet.available = form.available.data

        db.session.commit()

        return redirect(f"/{pet.id}")

    else:
        return render_template("pet_info.html", pet=pet, form=form)