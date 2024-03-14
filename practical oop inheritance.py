# Parent Class
class Animal:  
    def speak(self):  
        print("Animal Speaking" ,"(This is inside Parent class.)\n")  

# Child Class
class cat(Animal):  
    def bark(self):  
        print("Cat barking","(This is inside Child class.)\n")  
        
        
a = cat()  
a.bark()  
a.speak()  