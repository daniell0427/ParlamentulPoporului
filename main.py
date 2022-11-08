from flask import Flask, render_template, url_for
from form import RegisterForm, LoginForm

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
    return render_template("lege1.html")

@app.route("/inregistrare")
def inregistrare():
    form = RegisterForm()
    return render_template("register.html", form = form)

@app.route("/autentificare")
def autentificare():
    form = RegisterForm()
    return render_template("login.html", form = form)
    


@app.route("/adauga_proiect")
def adauga_proiect():
    return render_template("adauga_proiect.html")

if __name__ == "__main__":
    app.run(debug = True)
