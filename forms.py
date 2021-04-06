from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    """Sign up form"""

    username = StringField('Username', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])


class LoginForm(FlaskForm)    :
    """Login form"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
