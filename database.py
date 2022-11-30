import mysql.connector
from argon2 import PasswordHasher
verifi=0 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="legi"
)
# getting the cursor by cursor() method
def introdu(tit,pro1,contra1,neu1,pro2,contra2,neu2):
  mycursor = db.cursor()

  insertQuery = "INSERT INTO legi (titlu, pro_l1, contra_l1, neu_l1, pro_l2, contra_l2, neu_l2) VALUES ('"+tit+"',"+pro1+","+contra1+","+neu1+","+pro2+","+contra2+","+neu2+");"
  
  mycursor.execute(insertQuery)
  
  print("No of Record Inserted :", mycursor.rowcount)
  
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)
  
  # To ensure the Data Insertion, commit database.
  db.commit() 
  
  # close the Connection
 # db.close()

def titluri():
  mycursor = db.cursor()

  mycursor.execute("SELECT titlu FROM legi")

  myresult = mycursor.fetchall()

  return myresult


def inregistrare(user,email,password):
  mycursor = db.cursor()

  insertQuery = "INSERT INTO inregistrare (username, email, password) VALUES ('"+user+"','"+email+"','"+password+"');"
  
  mycursor.execute(insertQuery)
  
  print("No of Record Inserted :", mycursor.rowcount)
  
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)
  
  # To ensure the Data Insertion, commit database.
  db.commit()

def username():
  mycursor = db.cursor()

  mycursor.execute("SELECT username FROM inregistrare")

  myresult = mycursor.fetchall()

  return myresult

def verificare(camp,nume):
    mycursor = db.cursor()

    sql = "SELECT * FROM inregistrare WHERE "+camp+"='"+nume+"'"

    mycursor.execute(sql)
    ok=1
    myresult = mycursor.fetchall()
    
    if not(myresult):
      ok=0
    print(ok)
    return ok
def verify_password(self, password):
     hasher = PasswordHasher()
     try:
         hasher.verify(self, password)
         return True
     except Exception:
         return False

def verificare_pass(password,user):
    mycursor = db.cursor()

    sql = "SELECT password FROM inregistrare WHERE username ='"+user+"';"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    ph = PasswordHasher()
    a=verify_password(myresult[0][0],password)
    return a
  
def parola_nou(user,password):
    mycursor = db.cursor()

    sql = "UPDATE inregistrare SET password = '"+password+"' WHERE username = '"+user+"'"

    mycursor.execute(sql)

    db.commit()

def postare_db(titlu, descriere, username, data):
  mycursor = db.cursor()

  insertQuery = "INSERT INTO legipropuse (titlu, descriere, username, data) VALUES ('"+titlu+"','"+descriere+"','"+username+"', '"+data+"');"
  
  mycursor.execute(insertQuery)
  
  print("No of Record Inserted :", mycursor.rowcount)
  
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)
  
  # To ensure the Data Insertion, commit database.
  db.commit()

def get_id_lege(id):
  mycursor = db.cursor()
  sql = "SELECT * FROM legipropuse WHERE nr ='"+id+"'"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  titlu = myresult[0][1]
  descriere = myresult[0][2]
  username = myresult[0][3]
  data = myresult[0][4]
  insertQuery = "INSERT INTO legipr_admise (titlu, descriere, username, data) VALUES ('"+titlu+"','"+descriere+"','"+username+"', '"+data+"');"
  mycursor.execute(insertQuery)
  
  print("No of Record Inserted :", mycursor.rowcount)
  
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)
  
  # To ensure the Data Insertion, commit database.
  db.commit()

def get_legi(camp):
  mycursor = db.cursor()

  mycursor.execute("SELECT "+camp+" FROM legipr_admise")

  myresult = mycursor.fetchall()

  return myresult

def get_data_by_title(titlu):

  mycursor = db.cursor()

  mycursor.execute("SELECT * FROM legipr_admise WHERE titlu ='"+titlu+"'")

  myresult = mycursor.fetchall()

  return myresult

<<<<<<< HEAD
#Ciocan spala-te
=======
def cautar(caut):
  mycursor = db.cursor()

  mycursor.execute("SELECT titlu FROM legi WHERE titlu LIKE '%"+caut+"%'")

  myresult = mycursor.fetchall()

  return myresult
>>>>>>> 070cfc47d61f0b7451742557ecad02bf73a674fe
