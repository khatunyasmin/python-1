class num:
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def cal(self):
        print(self.n+self.m)
        print(self.n-self.m)
        print(self.n*self.m)
        print(self.n/self.m)
        print(self.n**self.m)
        print(self.n%self.m)
        print(self.n//self.m)
        
a=num(20,30) 
a.cal()   
        