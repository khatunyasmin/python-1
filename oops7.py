class minimum:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def small(self):
        if self.a<self.b:
            print("a is a smallest number",self.a)
        elif self.b<self.c:
            print("b is a smallest number",self.b)
        else:
            print("c is a smallest number",self.c)
               
m=minimum(20,10,60)
m.small()