import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Khan@123",database="db1")

str="delete from book where title='python3'"

cur=mycon.cursor()
cur.execute(str)
mycon.commit()