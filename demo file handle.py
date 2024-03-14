file_open = open("demo.txt","r+")

 

str1 = file_open.read(10)

 

print("Read the string: ",str1)

 


#check the current position

 

position = file_open.tell()

 

print ("File's current position: ",position)

 

#Reposition the file pointer at the beginning

 

position = file_open.seek(0,0)

 

str1 = file_open.read(5)

 

print("Reading again: ",str1)

 

file_open.close()