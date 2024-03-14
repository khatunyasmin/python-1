import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Khan@123",database="db1")
  
  #condition will be check
  
"""if mycon.is_connected():
    print("successfully connected")
    
cur=mycon.cursor()
#create a database
cur.execute("CREATE DATABASE db1")"""
#create a table

"""str="create table book(bookid integer(4),title varchar(20),price float(5,2))"

cur=mycon.cursor()
cur.execute(str)"""


#insert values into tables


str="insert into book(bookid,title,price) values (%s,%s,%s)"

b1=(101,"python3",450)
cur=mycon.cursor()
cur.execute(str,b1)
mycon.commit()













