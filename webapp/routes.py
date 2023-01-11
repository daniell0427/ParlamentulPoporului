from flask import render_template, url_for, redirect, request, session, flash
from webapp.form import inreg, autentificarea ,reset_pass, send_otp,inregistrare_changes_db
from webapp import app
from database import titluri, postare_db, get_legi, get_data_by_title, cautar, get_data_by_username,introdu,verificare_legi
from datetime import datetime
from flask_session import Session
import pandas as pd


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def global_variables():
    
    if session.get('username')!=None:
        global username
        global email
        global verified
        username = session.get('username')
        email = session.get('email')
        verified = get_data_by_username('verified', username)


@app.route("/")
@app.route("/acasa")
@app.route("/acasa/")
@app.route("/acasa/<titlu>")
def acasa(titlu=None):
    global_variables()
    titles=titluri()

    if titlu == None:
        titles=titluri()
        return render_template("index.html", len = len(titles),titles=titles)
    else:
        content = get_data_by_title("legi", titlu)
        titlu = content[0][1]
        if content[0][2] != None:
            pro_lect1 = content[0][2]
        else:
            pro_lect1 = 0

        if content[0][3] != None:
            con_lect1 = content[0][3]
        else:
            con_lect1 = 0
        
        if content[0][4] != None:
            neu_lect1 = content[0][4]
        else:
            neu_lect1 = 0
        
        if content[0][5] != None:
            pro_lect2 = content[0][5]
        else:
            pro_lect2 = 0

        if content[0][6] != None:
            con_lect2 = content[0][6]
        else:
            con_lect2 = 0
        
        if content[0][7] != None:
            neu_lect2 = content[0][7]
        else:
            neu_lect2 = 0
        return render_template("layout_lege.html", titlu=titlu, pro_lect1=pro_lect1, con_lect1=con_lect1, neu_lect1=neu_lect1, pro_lect2=pro_lect2, con_lect2=con_lect2, neu_lect2=neu_lect2)


@app.route("/inregistrare", methods=['GET', 'POST'])
def inregistrare():
    
    if session.get("username")  == None:
        e=""
        if request.method == "POST":
            global username
            username = request.form.get("user")
            global email
            email = request.form.get("email") 
            password = request.form.get("password") 
            pass_conf= request.form.get("pass_conf")
            global verified
            verified = "False"
            e=inreg(username,email,password,pass_conf,verified)
            if e!="Inregistrare completa": 
                print(e)
            else:
                #Verificare email:
                return redirect(url_for('email_verification'))
        return render_template("register.html" ,e=e)
    else:
        return redirect(url_for("acasa"))


@app.route("/autentificare", methods=['GET', 'POST'])
def autentificare():
    if session.get("username") == None:
        eror=""
        if request.method == "POST":
            global username
            username = request.form.get("user") 
            password = request.form.get("password") 
            global email
            print(username)
            print(password)
            if username=="Admin" and password=="parlamentulpoporului":
                session['username']="Admin"
                return redirect(url_for("admin"))
            else:
                email = get_data_by_username("email", username)
                eror=""
                eror = autentificarea(email, username,password)
                if eror=="" :
                    if username=="Admin" and password=="parlamentulpoporului":
                        return redirect(url_for("admin"))
                    else :
                        session["username"] = username
                        session["email"] = email
                    return redirect(url_for("acasa",user=username))
                        
        return render_template("login.html",e=eror)
    else:
        return redirect(url_for("acasa"))



@app.route("/account",methods=['GET', 'POST'])
def account():
    global email
    global username
    try:
        verified = get_data_by_username('verified', username)
    except:
        return render_template("except_page.html")
    return render_template("account.html", email = email, verified = verified)

@app.route("/reset-password",methods=['GET', 'POST'])
def reseteaza_parola():
    if session["username"] != None:
        e=""
        if request.method == "POST":
            password = request.form.get("password")
            password_new =request.form.get("new_pass")
            password_conf=request.form.get("conf_pass") 
            global email
            e=reset_pass(password, password_new, password_conf, email)  
            if e=="":
                return redirect(url_for("acasa"))
        return render_template("reseteazaparola.html",e=e)
    else:
        return redirect(url_for('acasa'))

# @app.route("/legi-propuse")
# @app.route("/legi-propuse/")
# @app.route("/legi-propuse/<titlu>")
# def legi_propuse(titlu=None):
#     if titlu == None:
#         titlu = get_legi("titlu")
#         descriere = get_legi("descriere")
#         username = get_legi("username")
#         data = get_legi("data")
#         nr = len(titlu)
#         return render_template("legi_propuse.html", title = "Legi Propuse", titlu=titlu, descriere=descriere, username=username, data=data, nr=nr)
#     else:
#         content = get_data_by_title("legipr_admise", titlu)
#         titlu = content[0][1]
#         descriere = content[0][2]
#         username = content[0][3]
#         data = content[0][4]
#         if content[0][5] != None:
#             pro = content[0][5]
#         else:
#             pro = 0

#         if content[0][6] != None:
#             contra = content[0][6]
#         else:
#             contra = 0
        
#         if content[0][7] != None:
#             neutru = content[0][7]
#         else:
#             neutru = 0
#         return render_template("layout_lege_propusa.html", title = "Legi Propuse", titlu=titlu, descriere=descriere, username=username, data=data, pro=pro, contra=contra, neutru=neutru)

# @app.route("/legi-recente")
# @app.route("/legi-recente/")
# @app.route("/legi-recente/<titlu>")
# def legi_recente(titlu=None):
#     if titlu == None:
#         titles=titluri()
#         return render_template("legi_recente.html", title = "Legi Recente", len=len(titles), titles=titles)
#     else:
#         content = get_data_by_title("legi", titlu)
#         titlu = content[0][1]
#         if content[0][2] != None:
#             pro_lect1 = content[0][2]
#         else:
#             pro_lect1 = 0

#         if content[0][3] != None:
#             con_lect1 = content[0][3]
#         else:
#             con_lect1 = 0
        
#         if content[0][4] != None:
#             neu_lect1 = content[0][4]
#         else:
#             neu_lect1 = 0
        
#         if content[0][5] != None:
#             pro_lect2 = content[0][5]
#         else:
#             pro_lect2 = 0

#         if content[0][6] != None:
#             con_lect2 = content[0][6]
#         else:
#             con_lect2 = 0
        
#         if content[0][7] != None:
#             neu_lect2 = content[0][7]
#         else:
#             neu_lect2 = 0
#         return render_template("layout_lege_recenta.html", titlu=titlu, pro_lect1=pro_lect1, con_lect1=con_lect1, neu_lect1=neu_lect1, pro_lect2=pro_lect2, con_lect2=con_lect2, neu_lect2=neu_lect2)


# @app.route("/propune-legi", methods=['GET', 'POST'])
# def propune_legi():
#     if session["username"] != None and verified == 'True':
#         if request.method == "POST":

#             titlu = request.form.get("titlu")
#             descriere = request.form.get("descriere")
#             username = session["username"]
#             now = datetime.now()
#             data = now.strftime('%d-%m-%Y')
#             postare_db(titlu, descriere, username, data)
#             if True:
#                 return redirect(url_for("acasa"))
#         return render_template("propune_legi.html", title = "Propune o lege")
#     else:
#         if session["username"] == None:
#             flash('Trebuie sa va autentificati pentru a accesa Propune Legi!', 'danger')
#             return redirect(url_for('autentificare'))
#         else:
#             flash('Trebuie sa va verificati email-ul pentru a accesa Propune Legi!', 'danger')
#             return redirect(url_for('legi_propuse'))

@app.route("/logout")
def logout():
    session["email"]=None
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
    return render_template("legi_recente.html", title = "Cautare",titles=a,len=len(a),c=c,b=b ,eror=eror)

@app.route("/verificare-email" , methods=["GET","POST"])
def email_verification():
    global email
    global verified
    if verified == 'False':
        msg = send_otp(email)
        if request.method == "POST":
            otp = request.form.get("otp")
            if otp == msg:
                try:
                    inregistrare_changes_db('verified', 'True', email)
                except:
                    print('Ne pare rau, a aparut o eroare! Incercati mai tarziu.')
                return redirect(url_for("autentificare"))
            else:
                print("Otp invalid")
    else:
        return redirect(url_for('acasa'))

    return render_template('email_verification.html', email=email, msg=msg)

@app.route("/admin" , methods=["GET","POST"])
def admin():
    if request.method == "POST":
        a=request.form.get("file1")
        print(a)
        data = pd.read_excel(a)
        tit=data['Denumire'].tolist()
        pro1=data['Lectura 1'].tolist()
        cont1=data['Unnamed: 2'].tolist()
        neu1=data['Unnamed: 3'].tolist()
        pro2=data['Lectura 2'].tolist()
        cont2=data['Unnamed: 5'].tolist()
        neu2=data['Unnamed: 6'].tolist()
        len1=len(tit)
        for i in range(1, len(tit) ):
            b=verificare_legi(tit[i])
            if b==0:
                introdu(str(tit[i]),str(pro1[i]),str(cont1[i]),str(neu1[i]),str(pro2[i]),str(cont2[i]),str(neu2[i]))
            print(b)
    return render_template("admin.html")