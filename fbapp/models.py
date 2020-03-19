from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app
import enum

# Create database connection object
db = SQLAlchemy(app)


class Gender(enum.Enum):
    female = 1
    male = 2
    other = 3


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


# database initialisation
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", Gender['male']))
    db.session.add(Content("What's your favorite scary movie?", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')
