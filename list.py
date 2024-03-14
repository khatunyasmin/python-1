"""mylist=[3,5,6,7,8,"hello"]
print(mylist[5])
print(mylist[5][4])
print(mylist[4:])

yasu=[5,4,7,10.5,"hi","bye",9,True,False,10]
print(yasu[:5])
print(yasu[-6:-4])
print(yasu[-1])
yasu.reverse()
print(yasu)"""
"""a=[8,9,6,7,5]
a.sort()
a.reverse()
print(a)"""



#list
lst = list(input("enter a value:")) #[23, 100, 54, 56, 98]

#interchanging the first and last element
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

