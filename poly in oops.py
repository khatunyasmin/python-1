class base:
    basevar = 50            # 525

    def __init__(self):
        print("Inside parent constructor")

    def basemethod(self):
        print("Inside base method")

    def setAttr(self,var1):     # var1 = 525
        base.basevar = var1     # basevar = 525

    def getAttr(self):
        print("Base Variable: ",base.basevar)


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

 

obj.getAttr()