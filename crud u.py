import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="Khan@123",database="db1")

str= "UPDATE book SET price=price-40 where price>500 "
cur=mycon.cursor()
cur.execute(str)
mycon.commit()