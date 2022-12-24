from flask import render_template, url_for, redirect, request, session, flash
from webapp.form import inreg, autentificarea ,reset_pass
from webapp import app, otp, mail
from database import titluri, postare_db, get_legi, get_data_by_title, cautar
from datetime import datetime
from flask_session import Session
from flask_mail import Message

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@app.route("/acasa")
def acasa():
    a=titluri()
    print(a)
    n=len(a)
    c=1
    b=0
    if n%2==0: c=0
    if n%2==0: b=1
    
    return render_template("index.html", len = len(a),a=a,c=c,b=b,)


@app.route("/inregistrare", methods=['GET', 'POST'])
def inregistrare():
    if session["username"] == None:
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
                msg = Message(subject='OTP', sender='parlamentulpoporului@gmail.com', recipients=[email])
                msg.body = str(otp)
                mail.send(msg)
                return render_template('email_verification.html', email=email)
        return render_template("register.html" ,e=e)
    else:
        return redirect(url_for("acasa"))


@app.route("/autentificare", methods=['GET', 'POST'])
def autentificare():
    if session["username"] == None:
        eror=""
        if request.method == "POST":
            user = request.form.get("user") 
            password = request.form.get("password") 
            eror=""
            eror = autentificarea(user,password)
            if eror=="" :
                session["username"] = user
                return redirect(url_for("acasa",user=user))

        return render_template("login.html",e=eror)
    else:
        return redirect(url_for("acasa"))


@app.route("/reseteaza-parola",methods=['GET', 'POST'])
def reseteaza_parola():
    if session["username"] == None:
        e=""
        if request.method == "POST":
            password = request.form.get("password")
            password_new =request.form.get("new_pass")
            password_conf=request.form.get("conf_pass") 
            user=session.get("username")
            e=reset_pass(password, password_new,password_conf, user)  
            if e=="":
                return redirect(url_for("acasa"))
        return render_template("reseteazaparola.html",e=e)
    else:
        return redirect(url_for('acasa'))

@app.route("/legi-propuse")
@app.route("/legi-propuse/")
@app.route("/legi-propuse/<titlu>")
def legi_propuse(titlu=None):
    if titlu == None:
        titlu = get_legi("titlu")
        descriere = get_legi("descriere")
        username = get_legi("username")
        data = get_legi("data")
        nr = len(titlu)
        return render_template("legi_propuse.html", title = "Legi Propuse", titlu=titlu, descriere=descriere, username=username, data=data, nr=nr)
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
def legi_recente():
    a=titluri()
    print("da")
    print(a)
    n=len(a)
    c=1
    b=0
    if n%2==0: c=0
    if n%2==0: b=1
    #print(user)
    return render_template("legi_recente.html", title = "Legi Recente", len=len(a),a=a,c=c,b=b)

@app.route("/legi-in-discutie")
def legi_in_discutie():
    return render_template("legi_in_discutie.html", title = "Legi in discutie")

@app.route("/propune-legi", methods=['GET', 'POST'])
def propune_legi():
    if session["username"] != None:
        if request.method == "POST":

            titlu = request.form.get("titlu")
            descriere = request.form.get("descriere")
            username = session["username"]
            now = datetime.now()
            data = now.strftime('%d-%m-%Y')
            postare_db(titlu, descriere, username, data)
            if True:
                return redirect(url_for("acasa"))
        return render_template("propune_legi.html", title = "Propune o lege")
    else:
        return redirect(url_for('autentificare'))

@app.route("/logout")
def logout():
    session["username"]=None
    return redirect(url_for("acasa"))

@app.route("/cautare", methods = ['POST'])
def cautare():
    
    if request.method == "POST":
        caut = request.form.get("caut")
        
        a=cautar(caut)
    eror=""
    n=len(a)
    if n==0:
        eror="Ne pare rau nu sa gasit nicio lege"
    print(n)
    c=1
    b=0
    if n%2==0: c=0
    if n%2==0: b=1
    return render_template("legi_recente.html", title = "Cautare",a=a,len=len(a),c=c,b=b ,eror=eror)

