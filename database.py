import mysql.connector
  
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
  i=1
  return myresult
  #for x in myresult:
   # legi[i]=x
   # i=i+1
   # print(x)

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
  i=1
  return myresult

def verificare(camp,nume):
    mycursor = db.cursor()

    sql = "SELECT * FROM inregistrare WHERE "+camp+"='"+nume+"'"

    mycursor.execute(sql)
    ok=1
    myresult = mycursor.fetchall()
    
    if myresult:
      ok=0
    print(ok)
    return ok