class num:
    def __init__(self,r):
        self.r=r
    def rad(self):
        print(2*self.r)
        print(2*3.14*self.r)
        print(3.14*self.r*self.r)
c=num(12)
c.rad()