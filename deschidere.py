from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/home")
def index():
    """Serve homepage template."""
    return render_template("index.html")
@app.route("/inregistrare")
def form():
    """Serve homepage template."""
    return render_template("form.html")