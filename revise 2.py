# try:
#     num=50
#     den=5
#     output=num/den
#     print(output)
# except:
#     print("cannot divide by zero")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a number.")
# finally:
#     print("Exception handling completed.")
   
class man:#man is class name
    def __init__(self,exp,name): # def is function ,__init__ is constructor,self is reference of object variable,(exp,name is parameter)
        self.exp=exp
        self.name=name
    def show(self):# show is function name
        print(self.exp)
        print(self.name)
        
obj1=man(21,"yasmin")#obj1 is object name ,(21,yasmin is argument a putting value of constructor parameter)
obj1.show() #calling function
   
obj2=man(20,"tinu")
obj2.show()   