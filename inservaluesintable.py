#using this file to insert data into my table Subscribers created in mysql

import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="manolaAA123!",
    database="data_representation"
)

cursor=db.cursor()
sql="insert into subscribers (Name,Paid) values (%s,%s)"
values=("Carmen",38, 456)

cursor.execute(sql,values)

db.commit()
print("record inserted, ID:",cursor.lastrowid)
