from database import inregistrare , verificare , verificare_pass , inregistrare_changes_db
from argon2 import PasswordHasher
from flask_mail import Message
from webapp import otp, mail

def password_hash(pass1):
    ph = PasswordHasher()
    hash = ph.hash(pass1)
    return hash


def inreg(user, email, phone, password, conf_pass, verified):
    e=""
    if user != None:
        a=verificare("username",user)
        if a: 
            e=e+" Acest nume de utilizator este folosit! "

    a=verificare("email", email)
    if a:
        e=e+" Acest email este deja folosit! "

    phone_nr = phone_restructure(str(phone))
    a=verificare("phone", phone_nr)
    if a:
        e=e+" Acest numar de telfon este deja folosit! "
    if password!=conf_pass :
        e=e+" Parola Gresita "
    if e=="":
        passwordh=password_hash(password)
        inregistrare(user,email,phone_nr,passwordh,verified)
        e="Inregistrare completa"
    return e

def phone_restructure(phone_nr):
    if phone_nr[0] == '+':
        nr_restr = phone_nr
    elif phone_nr[0] == '0':
        nr_restr = '+373' + phone_nr[1:]
    else:
        nr_restr = '+373' + phone_nr
    print(nr_restr)
    return nr_restr
    

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
