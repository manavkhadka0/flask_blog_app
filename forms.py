from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length




class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators = [DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign UP')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
