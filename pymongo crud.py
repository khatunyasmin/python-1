#python mongodb connectivity and crud operation

import pymongo

client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create 
mydb=client["pythondb1"]

#create a collection

mycollection=mydb["sample_coll"]


#create a document

"""mydoc={"name":"yasmin","lastname":"khan"}


#insert a the document
res=mycollection.insert_one(mydoc)


#print(client.list_database_names())



#read the document


record=mycollection.find_one()
print(record)


#update the record

query={"lastname":"khan"}

new_val={"$set":{"lastname":"khatun"}}

new_doc=mycollection.update_one(query,new_val)

print(new_doc)

#how to update value showing

doc_update=mycollection.find_one()
print(doc_update)"""


#delete the records
query_del={'name':'yasmin'}

doc_del=mycollection.delete_one(query_del)


#reading 
x=mycollection.find_one()
print(x)

