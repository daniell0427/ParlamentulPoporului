from database import inregistrare , verificare , verificare_pass , inregistrare_changes_db
from argon2 import PasswordHasher
from flask_mail import Message
from webapp import otp, mail

def password_hash(pass1):
    ph = PasswordHasher()
    hash = ph.hash(pass1)
    return hash


def inreg(user, email, password, conf_pass, verified):
    e=""
    a=verificare("username",user)
    if a: 
        e=e+" Acest nume de utilizator este folosit "
    a=verificare("email", email)
    if a:
        e=e+" Sunteti deja inregistrat "
    if password!=conf_pass :
        e=e+" Parola Gresita "
    if e=="":
        passwordh=password_hash(password)
        inregistrare(user,email,passwordh,verified)
        e="Inregistrare completa"
    return e

def autentificarea(email, user, password):
    e=""
    a=verificare("username",user)
    if not(a):
        e=e+"Acest nume de utilizator nu exista"
    else :
        a=verificare_pass(password, email)
        if a==True:
            e=""
        else:
            e="Parola gresita" 
    return e

def reset_pass(password_old,password,conf_password,email):
    a=verificare_pass(password_old, email)
    e=""
    if a==True:
        if password==conf_password :
            pas=password_hash(password)
            a=inregistrare_changes_db('password', pas, email)
        else:
            e="Parloa de confirmare gresita"
    else :
        e="parola gresita"
    return e

def user_in_db(user):
    error = ''
    a = verificare("username", user)
    if not(a):
        error = "Aceasta pagina este invalida"
    else:
        error = ''
    return error

def send_otp(email):
    msg = Message(subject='OTP', sender='parlamentulpoporului@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return str(otp)
