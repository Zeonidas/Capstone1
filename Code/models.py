# Start Imports
from email.mime import image
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

DEFAULT_IMAGE = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

######################################################################
# Making classes

class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer, 
        primary_key=True)
        
    username = db.Column(
        db.String(15), 
        nullable=False, 
        unique=True)

    password = db.Column(
        db.Text, 
        nullable=False)

    image_url = db.Column(
        db.Text, 
        nullable=False, 
        default=DEFAULT_IMAGE)
 

    journals = db.relationship('Journal')

    @classmethod
    def register(cls, username, password, image_url):
        """Register new user"""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username = username,
            password = hashed_pwd,
            image_url = image_url,
    )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """User login
        Finds username and password.
        Returns failure if nothing can be found."""

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

    @classmethod
    def register(cls, username, password, image_url):
        """Register new user"""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username = username,
            password = hashed_pwd,
            image_url = image_url
        )

        db.session.add(user)
        return user
        
class Journal(db.Model):
    """Journal"""

    __tablename__ = "journals"

    id = db.Column(
        db.Integer, 
        primary_key=True
        )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable = False
    )
    title = db.Column(
        db.String(120), 
        default="No Title")

    entry = db.Column(
        db.String(1500))

    date = db.Column(
        db.DateTime, 
        nullable=False, 
        default=datetime.utcnow())

    user = db.relationship('User')

class Questions(db.Model):
    """Questions"""

    __tablename__ = "questions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    question = db.Column(
        db.Text
    )


def connect_db(app):
    """Connect to the database"""

    db.app = app
    db.init_app(app)

