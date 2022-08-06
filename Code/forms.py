from dataclasses import dataclass
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistrationForm(FlaskForm):
    """Registration Form for new users"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8, max=32)])
    image_url = StringField('(Optional) Add your image here')

class UserLoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class JournalEntryForm(FlaskForm):

    title = StringField('Title', validators=[Length(max=120)])
    entry = TextAreaField('Entry', validators=[Length(max=1500)])

class QuestionnaireForm(FlaskForm):
    selResponse = RadioField('Feeling', choices=[
        ("0", "Not at all"), ("1", "Several Days"), ("2", "More than half the days"), ("3", "Nearly every day")], validate_choice=DataRequired())
