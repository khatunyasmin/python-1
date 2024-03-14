class counter1:
    __secretcount=0
    
    
    
    def count(self):
        self.__secretcount+=1
        print(self.__secretcount)
        
c=counter1()

c.count()

c.count()
print(c.__secretcount)
