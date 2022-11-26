from flask import render_template, url_for, flash, redirect,request
from webapp.form import inreg, autentificarea ,reset_pass
from webapp import app
from database import titluri, inregistrare ,verifi, postare_db
from datetime import date, datetime


@app.route("/")
@app.route("/acasa/<user>")

def acasa(user=None):
    a=titluri()
    print(a)
    n=len(a)
    c=1
    b=0
    if n%2==0: c=0
    if n%2==0: b=1
    
    print(user)
    return render_template("index.html",user=user, len = len(a),a=a,c=c,b=b)


@app.route("/inregistrare", methods=['GET', 'POST'])
def inregistrare():
    e=""
    if request.method == "POST":
       
       user = request.form.get("user")
       email = request.form.get("email") 
       password = request.form.get("password") 
       pass_conf= request.form.get("pass_conf")
       e=inreg(user,email,password,pass_conf)
       if e!="Inregistrare completa": 
           print(e)
       else:
           return redirect(url_for("autentificare"))
       
    return render_template("register.html" ,e=e)


@app.route("/autentificare", methods=['GET', 'POST'])
def autentificare():
    eror=""
    if request.method == "POST":
        user = request.form.get("user") 
        password = request.form.get("password") 
        eror=""
        eror=autentificarea(user,password )
        if eror=="" :
            
            return redirect(url_for("acasa",user=user))

    return render_template("login.html",e=eror)


@app.route("/reseteaza-parola/<user>",methods=['GET', 'POST'])
def reseteaza_parola(user):
    e=""
    if request.method == "POST":
      
      password = request.form.get("password")
      password_new =request.form.get("new_pass")
      password_conf=request.form.get("conf_pass") 
      e=reset_pass(password, password_new,password_conf, user)  
      if e=="":
        return redirect(url_for("acasa",user=user))
    
    return render_template("reseteazaparola.html",e=e)


@app.route("/legi-propuse/<user>")
def legi_propuse(user=None):
    print(user)
    return render_template("legi_propuse.html", title = "Legi Propuse",user=user)

@app.route("/legi-recente/<user>")
def legi_recente(user=None):
    a=titluri()
    print("da")
    print(a)
    n=len(a)
    c=1
    b=0
    if n%2==0: c=0
    if n%2==0: b=1
    #print(user)
    return render_template("legi_recente.html", title = "Legi Recente",user=user, len=len(a),a=a,c=c,b=b)

@app.route("/legi-in-discutie/<user>")
def legi_in_discutie(user=None):
    return render_template("legi_in_discutie.html", title = "Legi in discutie",user=user)

@app.route("/propune-legi", methods=['GET', 'POST'])
def propune_legi():
    if request.method == "POST":

        titlu = request.form.get("titlu")
        descriere = request.form.get("descriere")
        username = "nume"
        now = datetime.now()
        data = now.strftime('%Y-%m-%d')
        postare_db(titlu, descriere, username, data)
        if True:
            return redirect(url_for("acasa"))
    return render_template("propune_legi.html", title = "Propune o lege")