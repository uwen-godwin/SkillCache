from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username cannot be blank")])
    email = StringField('Email', validators=[DataRequired(message="Email cannot be blank"), Email(message="Invalid email address")])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password cannot be empty"),
        Length(min=8, message="Password must be at least 8 characters long")
    ])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please confirm your password"),
        EqualTo('password', message="Passwords must match")
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Email cannot be blank"), Email(message="Invalid email address")])
    password = PasswordField('Password', validators=[DataRequired(message="Password cannot be empty")])
    submit = SubmitField('Login')
