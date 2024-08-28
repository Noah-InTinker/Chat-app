
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username', validators=[DataRequired(), Length(1, 63)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me =BooleanField('Keep me logged in')
    submit = SubmitField('Login')
    
    

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('username', validators=[DataRequired(), Length(1, 63)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Register')