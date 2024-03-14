"""list=[1,2,3,4,5]
for i in range(len(list)):
    list[i]=list[i]*list[i]
    list.reverse()
print(list)"""
a=[4,5,7,6,3,2]
a=eval(input("Enter a number:"))
a.reverse()
for x in a:
    b=x*x
    print(b)  