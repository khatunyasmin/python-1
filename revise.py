# dict1={'name':'yasu','age':20,'city':'Bbsr'}
# dict1['state']='odisha'
# print(dict1)

# dict2={'a1':20,'a2':30,'a3':40}
# print(dict2['a1']+dict2['a2']+dict2['a3'])

# tuple1=(1,25,3,25,4,25,6,25)
# check=tuple1.count(25)
# print("Count the number of occurrences of 25 from a tuple.",check)
print("Hello world!")
name = "John"
age = 25
print(type(name))
print(age)
fruits = ["apple", "banana", "cherry"]
print(type(fruits))

def fn1():
    name="yasu"
    print("hello,"+ name)
fn1()
age =int(input("enter a age:" ))
if age < 18:
    print("You're underage.")
elif age == 18:
    print("You're just 18.")
else:
    print("You're an adult.")
    
for i in range(10):
    print(i)
# count = 0
# while count < 5:
#     print(count)
#     count += 1
c = (10, 20,"yasu")
print(type(c))
colors = {"red", "green", "blue"}
print(type(colors))
a=True
print(type(a))
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num > 5:
        break
    print(num)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 == 0:
        continue
    print(num)


    
