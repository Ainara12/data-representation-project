#using this file to insert data into my table Subscribers created in mysql and test my connection


import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="manolaAA123!",
    database="data_representation"
)

cursor=db.cursor()
sql="insert into subscribers (Name,Paid,Membership) values (%s,%s,%s)"
values=("Stephanie",34, 123)

cursor.execute(sql,values)

db.commit()
print("record inserted, ID:",cursor.lastrowid)
