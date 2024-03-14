class base:
    basevar = 50            

    def __init__(self):
        print("Inside parent constructor")

    def basemethod(self):
        print("Inside base method")

    def setAttr(self,var1):     
        base.basevar = var1    

    

class derived(base):

    def __init__(self):
        print("Inside Child class contructor")

    def childmethod(self):
        print("Inside child method")

objbase = base()

obj = derived()

 

obj.childmethod()

 

obj.basemethod()

 

obj.setAttr(525)

 

