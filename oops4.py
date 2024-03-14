class num:
    def __init__(self,c):
        self.c=c
    def cm(self):
        print("convert into meter", self.c/100)
        print("convert into kilometer",self.c/100000)

m=num(1000)
m.cm()