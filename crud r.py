import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Khan@123",database="db1")

str="select * from book"
cur=mycon.cursor()
cur.execute(str)
result=cur.fetchall()

for rec in result:
    print(rec)