from database import inregistrare , verificare , verificare_pass , parola_nou
from argon2 import PasswordHasher
def password_hash(pass1):
    ph = PasswordHasher()
    hash = ph.hash(pass1)
    return hash


def inreg( user, email,password ,conf_pass):
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
        inregistrare(user,email,passwordh)
        e="Inregistrare completa"
    return e

def autentificarea(user, password):
    e=""
    a=verificare("username",user)
    if not(a):
        e=e+"Acest nume de utilizator nu exista"
    else :
        a=verificare_pass(password, user)
        if a==True:
            e=""
        else:
            e="Parola gresita" 
    return e

def reset_pass(password_old,password,conf_password ,user):
    a=verificare_pass(password_old,user)
    e=""
    if a==True:
        if password==conf_password :
            pas=password_hash(password)
            a=parola_nou(user,pas)
        else:
            e="Paroa de confirmare gresita"
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
