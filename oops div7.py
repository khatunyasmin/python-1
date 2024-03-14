class num:
    def __init__(self,x):
        self.x=x
    
       
    def show(self):
           for i in self.x:
            if i%7==0:
                print( i )
                
                
a=num(range(1,71))
a.show()                