from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo
from webapp.models import User


class RegisterForm(FlaskForm):
    username = StringField('Nume de utilizator', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Parola', 
                        validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirma Parola', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Inregistreaza-te')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Acest nume este deja luat')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Acest email este deja luat')

class LoginForm(FlaskForm):
    email = EmailField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Parola', 
                        validators=[DataRequired()])
    rememberme = BooleanField('Tine-ma minte')
    submit = SubmitField('Autentificare')

class ResetPassForm(FlaskForm):
    email = EmailField('Email', 
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Reseteaza Parola')
