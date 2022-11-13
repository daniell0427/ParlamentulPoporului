from webapp.form import RegisterForm, LoginForm, ResetPassForm
from flask import render_template, url_for, flash, redirect
<<<<<<< HEAD
from webapp import app, db, bcrypt
from webapp.models import User
=======
from webapp import app
from database import titluri
>>>>>>> c251dda763d0026f201f7b5fd492323e75ba2a74

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
    print (c)
    return render_template("index.html", len = len(a),a=a,c=c,b=b)


<<<<<<< HEAD
=======
@app.route("/lege1")
def lege1():
    return render_template("lege1.html", title = "Legi")

>>>>>>> c251dda763d0026f201f7b5fd492323e75ba2a74
@app.route("/inregistrare", methods=['GET', 'POST'])
def inregistrare():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Contul tau a fost creat cu succes!', 'success')
        return redirect(url_for('autentificare'))
    return render_template("register.html", form = form, title = "Inregistrare")


@app.route("/autentificare", methods=['GET', 'POST'])
def autentificare():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ciocandaniel45@gmail.com' and form.password.data == 'parola':
            flash('Logare cu succes!', 'success')
            return redirect(url_for('acasa'))
        else:
            flash('Autentificare invalida. Va rugam sa verificati emailul si parola', 'danger')
    return render_template("login.html", form = form, title = "Autentificare")
    

@app.route("/adauga-proiect")
def adauga_proiect():
    return render_template("adauga_proiect.html", title = "Adauga Proiect")


@app.route("/reseteaza-parola")
def reseteaza_parola():
    form = ResetPassForm()
    if form.validate_on_submit():
        return redirect(url_for('#'))
    return render_template("reseteazaparola.html", title = "Reseteaza Parola", form = form)


@app.route("/legi-propuse")
def legi_propuse():
    return render_template("legi_propuse.html", title = "Legi Propuse")

@app.route("/legi-recente")
def legi_recente():
    return render_template("legi_recente.html", title = "Legi Recente")

@app.route("/legi-in-discutie")
def legi_in_discutie():
    return render_template("legi_in_discutie.html", title = "Legi in discutie")