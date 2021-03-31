"""Models for Park Finder app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User"""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "users" 

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    favorite_parks = db.relationship("Favorite_Park", secondary="users_parks", backref="users") 


class Favorite_Park(db.Model):
    """Favorite Park"""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "favorite_parks"

    park_id = db.Column(db.Integer, primary_key=True)

    users = db.relationship("User", secondary="users_parks", backref="favorite_parks")  


class UserPark(db.Model):
    """Mapping of a user to a park"""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "users_parks" 
    
    user_id = db.Column(db.Integer, db.ForeignKey("favorite_parks.id"))
    park_id = db.Column(db.Integer, db.ForeignKey("users.id")) 


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
