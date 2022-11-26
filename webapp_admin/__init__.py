from flask import Flask

app = Flask(__name__)   
 
from webapp_admin import routes_admin