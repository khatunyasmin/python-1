class stu:
    'comment base for all student'
    a=0
    def __init__(self,n,m):
        self.name = n      
        self.marks= m
        stu.a= stu.a+1
        
    def displaycount(self):

       print("Total students %d"%stu.a)   
       
    def displaystu(self):
        print("Name: ",self.name,",Marks:",self.marks)      

stu1=stu("yasmin",95)

stu2=stu("arpita",90)

#stu1.displaystu()
#stu2.displaystu()
#stu1.displaycount()
#stu2.displaycount()
#print("Total students %d"%stu.a)

"""stu1.marks=59
stu2.marks=89
stu1.name="yasu"
stu1.displaystu()
stu2.displaystu()"""
print("stu.__doc__:",stu.__doc__)
print("stu.__name__:",stu.__name__)
print("stu.__module__:",stu.__module__)
print("stu.__bases__:",stu.__bases__)
print("stu.__dict__:",stu.__dict__)

