class superclass:
    def method1(self):
        print("inside parent class method")
        
        
class childclass(superclass):
    def method1(self):
        print("inside childclass method")
        
        
        
x=childclass()

x.method1() #overwriting