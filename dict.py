dict={"Name":"yasu","age":25,"salary":40000,"oocupation":"manager"}
print(dict["Name"])
print(dict["salary"])
print(len(dict))



try:
	dict["age"]
	print('The key exists in the dictionary')
except KeyError as error:
	print("The key doesn't exist in the dictionary")

   

