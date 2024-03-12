# Python supports three programming paradigms- Structured programming, Functional programming and Object-oriented programming(OOP).
# What are Classes and Objects?
'''Class is like design/blueprint/format let suppose of building and building is the object'''

a = 'abc'                   # a is an object of str class
b = 3.14                    # b is an object of float class
lst = [1,2,3,4]             # lst is an object of list class
tpl = ('a','b','c','d')     # tpl is an object of tuple class

class employee:
    
    def sdata(self,n,p):              # In terms of the class we call functions as method. So sdata() and display() are the method.
        self.name = n                 # [**Note: Here 'self' is used to identify which objects data is being kept inside the method.(We can say it as object oriented method)]
        self.age = p
        
    def display(self):
        print('Name =',self.name,'\nAge =',self.age)
    
e1 = employee() 
e1.sdata('Ashok',23) 
e1.display()  
