from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    nume_utilizator = StringField('Nume de utilizator', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', 
                        validators=[DataRequired(), Email()])
    parola = PasswordField('Parola', 
                        validators=[DataRequired()])
    confirma_parola = PasswordField('Confirma Parola', 
                        validators=[DataRequired(), EqualTo(parola)])
    submit = SubmitField('Trimite')


class LoginForm(FlaskForm):
    email = EmailField('Email', 
                        validators=[DataRequired(), Email()])
    parola = PasswordField('Parola', 
                        validators=[DataRequired()])
    rememberme = BooleanField('Tine-ma minte')
    submit = SubmitField('Autentificare')