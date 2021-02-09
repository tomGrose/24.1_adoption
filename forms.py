from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange





class PetForm(FlaskForm):
    """Form for adding/editing Pet."""

    name = StringField("Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
                        validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                        validators=[Optional(), URL()])
    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(min=0, max=30, message="Age Must be between 0 and 30")])
    notes = StringField("Notes",
                        validators=[Optional()])

class UpdatePetForm(FlaskForm):
    """Form for updating a pets info"""

    photo_url = StringField("Photo URL",
                        validators=[Optional(), URL()])
    notes = StringField("Notes",
                        validators=[Optional()])
    available = BooleanField("Is the pet still available?",
                        validators=[Optional()])