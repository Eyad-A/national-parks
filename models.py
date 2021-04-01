"""Models for National Parks app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User"""

    __tablename__ = "users" 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    parks = db.relationship("Park", secondary="users_parks", backref="user") 

    def __repr__(self):
        return f"<User {self.user_name}>"


class Park(db.Model):
    """Park"""

    __tablename__ = "parks"

    id = db.Column(db.Integer, primary_key=True)

    users = db.relationship("User", secondary="users_parks", backref="parks")  

    def __repr__(self):
        return f"<Park {self.id}>"


class UserPark(db.Model):
    """Mapping of a user to a park"""

    __tablename__ = "users_parks" 
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey("parks.id"), primary_key=True) 


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
