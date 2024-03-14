class num:
    def __init__(self,n):
        self.n=n
    def show(self):
        if(self.n%7==0):
            print("it  is visible by seven")
        else:
            print("it is not visible by 7")
            
            
            
a=num(21)
a.show()