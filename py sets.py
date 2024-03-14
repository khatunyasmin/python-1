#python sets


id1={110,235,546,125,74,85}
list1=["a","b","c","d","e"]
set1=set(list1)
print(set1)


#how to add elements

set1.add("welcome")
print(set1)

#remove an element
set1.discard("welcome")
print(set1)

#update python sets

companies={'x','y'}
tech=['r','s','t']
companies.update(tech)
print(companies)
