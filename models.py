from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for creating a pet"""

    __tablename__ = "pets"

    def __repr__(self):
        """ Show info about a pet"""
        return f"<Name {self.name} Species: {self.species}>"

    

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text, 
                        nullable=True, default="https://bit.ly/2Z38coi")
    age = db.Column(db.Integer,
                    nullable = True)
    notes = db.Column(db.Text,
                     nullable=True)
    available = db.Column(db.Boolean,
                            default=True)


   