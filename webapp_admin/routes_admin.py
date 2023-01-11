from webapp_admin import app
from flask import request, render_template 
from database import *
import pandas as pd

@app.route('/', methods =["GET", "POST"])

def gfg():
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