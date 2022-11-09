from flask import Flask, render_template, url_for, flash, redirect
from form import RegisterForm, LoginForm, ResetPassForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '969bde9448eb7e83012c9d5d8d0f0ada'

articole = [
    {
    'titlu': '',
    'nume': '',
    'data': '',
    'text': ''
    }
]
    
@app.route("/")
@app.route("/acasa")
def acasa():
    return render_template("index.html")


@app.route("/lege1")
def lege1():
    return render_template("lege1.html", title = "Legi")


@app.route("/inregistrare", methods=['GET', 'POST'])
def inregistrare():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Cont creat pentru {form.nume_utilizator.data}!', 'success')
        return redirect(url_for('acasa'))
    return render_template("register.html", form = form, title = "Inregistrare")


@app.route("/autentificare", methods=['GET', 'POST'])
def autentificare():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ciocandaniel45@gmail.com' and form.parola.data == 'parola':
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


if __name__ == "__main__":
    app.run(debug = True)
