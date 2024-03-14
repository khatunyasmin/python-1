


class base:
    basevar =50
    
    def __init__(self):
        print("inside constructor")
        
    def basemethod(self):
        print("inside basemethod")
        
    def setAttr(self,var1):
        base.basevar=var1
        
    def getAttr(self):
        print("Base variable:",base.basevar)
        
        
class derived(base):
      
    def __init__(self):
        print("inside child class constructor")
        
    def childmethod(self):
        print("inside child method")
        
objbase=base() 


obj= derived()

obj.childmethod()

obj.basemethod()

obj.setAttr(525)
obj.getAttr()



        