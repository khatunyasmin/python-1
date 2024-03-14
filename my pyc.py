for x in "yasmin": #loop in a string
    print(x)
    
a=" Hello , yasmin " #check a string
print("Khan" in a)

print(a[2:5])# slicing

print(a[:6])#slice from the strat

print(a[6:]) #slice to the end
print(a.upper()) #all 
print(a.lower())
print(a.strip())
print(a.replace("yasmin","yasu"))


print(a.split(","))

c="hi"
d="bye"
e=c+" ,"+d
print(e)


age=22
amount=4000
a="my money {1} and old {0}."
print(a.format(age,amount))

#escape string 
b='i\'am yasu'
a= 'hello \byasu'
print(a)
print (b)