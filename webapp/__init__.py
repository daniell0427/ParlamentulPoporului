from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '969bde9448eb7e83012c9d5d8d0f0ada'    

from webapp import routes
