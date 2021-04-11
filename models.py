"""Models for National Parks app."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt() 
db = SQLAlchemy()


class User(db.Model):
    """User"""

    __tablename__ = "users" 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    parks = db.relationship("Park", secondary="users_parks", backref="user") 

    
    # class methods 

    @classmethod
    def signup(cls, username, password):
        """Signup a user and hash their password"""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8") 
        user = cls(
            username = username,
            password = hashed_utf8
        )

        db.session.add(user) 
        return user 

    
    @classmethod
    def authenticate(cls, username, password):
        """validate that user exists and password is correct"""

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user 
        else: 
            return False 


    def __repr__(self):
        return f"<User {self.username}>"


class Park(db.Model):
    """Park"""

    __tablename__ = "parks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    park_code = db.Column(db.String(4), unique=True, nullable=False)
    full_name = db.Column(db.Text, nullable=True) 
    main_image_url = db.Column(db.Text, nullable=True) 

    users = db.relationship("User", secondary="users_parks", backref="favorite_parks")  

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
