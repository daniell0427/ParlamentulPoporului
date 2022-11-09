import mysql.connector


def introdu(titi, pro_1, contra_1, neu_1, pro_2, contra_2, neu_2):


  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="legi"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO customers (titlu, pro_l1, contra_l1, neu_l1, pro_l2, contra_l2, neu_l2) VALUES (%s, %s, %s, %s, %s, %s, %s,)"
  val = (titi,pro_1,contra_1,neu_1,pro_2,contra_2,neu_2)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

introdu()