from flask import render_template, url_for, redirect,request
from webapp.form import inreg, autentificarea ,reset_pass, user_in_db
from webapp import app
from database import titluri, postare_db, get_legi, get_data_by_title
from datetime import datetime
@app.route("/")
@app.route("/<user>")
@app.route("/acasa")

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
        eror = autentificarea(user,password)
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

@app.route("/legi-propuse")
@app.route("/legi-propuse/")
@app.route("/legi-propuse/<titlu>")
def legi_propuse(titlu=None, user=None):
    if titlu == None:
        titlu = get_legi("titlu")
        descriere = get_legi("descriere")
        username = get_legi("username")
        data = get_legi("data")
        nr = len(titlu)
        print(user)
        return render_template("legi_propuse.html", title = "Legi Propuse",user=user, titlu=titlu, descriere=descriere, username=username, data=data, nr=nr)
    else:
        content = get_data_by_title(titlu)
        titlu = content[0][1]
        descriere = content[0][2]
        username = content[0][3]
        data = content[0][4]
        if content[0][5] != None:
            pro = content[0][5]
        else:
            pro = 0

        if content[0][6] != None:
            contra = content[0][6]
        else:
            contra = 0
        
        if content[0][7] != None:
            neutru = content[0][7]
        else:
            neutru = 0
        return render_template("lege_layout.html", title = "Legi Propuse", titlu=titlu, descriere=descriere, username=username, data=data, pro=pro, contra=contra, neutru=neutru)

@app.route("/legi-recente")
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

@app.route("/legi-in-discutie")
def legi_in_discutie(user=None):
    return render_template("legi_in_discutie.html", title = "Legi in discutie",user=user)

@app.route("/propune-legi", methods=['GET', 'POST'])
def propune_legi():
    if request.method == "POST":

        titlu = request.form.get("titlu")
        descriere = request.form.get("descriere")
        username = "nume"
        now = datetime.now()
        data = now.strftime('%d-%m-%Y')
        postare_db(titlu, descriere, username, data)
        if True:
            return redirect(url_for("acasa"))
    return render_template("propune_legi.html", title = "Propune o lege")

