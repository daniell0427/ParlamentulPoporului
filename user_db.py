from webapp import db

# getting the cursor by cursor() method
def introdu(username, email, password):
  mycursor = db.cursor()

  insertQuery = "INSERT INTO inregistrare (username, email, password) VALUES ("+username+","+email+","+password+");"
  
  mycursor.execute(insertQuery)
  
  print("No of Record Inserted :", mycursor.rowcount)
  
  # we can use the id to refer to that row later.
  print("Inserted Id :", mycursor.lastrowid)
  
  # To ensure the Data Insertion, commit database.
  db.commit() 
  
  # close the Connection
 # db.close()
