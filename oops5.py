class num: 
    def __init__(self,t,t1):
        self.t=t
        self.t1=t1
        
    def temp(self):
        print("celcius to farenheit",(9*self.t/5)+32)
        print("farenhit to celcius",(self.t1-32)*5/9)
        
        
        
a=num(10,66)
a.temp()