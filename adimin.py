
# importing Flask and other modules

from flask import Flask, request, render_template 
from database import *
 
# Flask constructor

app = Flask(__name__)   
 
# A decorator used to tell the application
# which URL is associated function


@app.route('/', methods =["GET", "POST"])

def gfg():

    if request.method == "POST":

       # getting input with name = fname in HTML form

       tit = request.form.get("titlu")

       # getting input with name = lname in HTML form 

       pro1 = request.form.get("pro_l1") 
       contra1 = request.form.get("contra_l1") 
       neu1 = request.form.get("neu_l1") 
       pro2 = request.form.get("pro_l2") 
       contra2 = request.form.get("contra_l2") 
       neu2 = request.form.get("neu_l2") 
       print(tit)
       print(pro1)
       print(contra1)
       print(neu1)
       print(pro2)
       print(contra2)
       print(neu2)
       introdu(tit,pro1,contra1,neu1,pro2,contra2,neu2)

    return render_template("admin.html")
 

if __name__=='__main__':

   app.run()
 