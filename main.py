from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return render_template("form.html")

@app.route("/adauga_proiect")
def adauga_proiect():
    return render_template("adaugaProiect.html")

if __name__ == "__main__":
    app.run(debug = True)
