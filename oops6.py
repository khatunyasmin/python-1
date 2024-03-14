class num:
    def __init__(self,n):
        self.n=n
    def show(self):
        if(self.n%2==0):
            print("it  is an even number")
        else:
            print("it is an odd number")
            
            
            
a=num(21)
a.show()