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