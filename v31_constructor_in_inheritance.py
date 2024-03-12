# Constructors

class A:                           # super class a
    def __init__(self):
        print('In init A')
    def cl1(self):
        print('Class A')
    
        
class B(A):                        # Derived class/Sub class
    def cl2(self):
        print('Class B')

# b1 = B()            # Here when we are creating an object of B it is calling init function of the class A 


# 2nd example

class C:
    
    def __init__(self):                      # Super class
        print('In init C')
    
    def in2(self):
        print('class C')

class D(C):
    
    def __init__(self):   
        super().__init__()               # By using super() function(built-in) we can call the function of the super class 
        print('In init D')
        super().in2()                    # We can use it to call any functiion
        
    def in3(self):
        print('class D')

# d1 = D()                # Here when we are creating an object of D it is calling init function of the class D only.
'''
Object of D try to find the init function(constructor) from the Class D if it cannont find init in the D then it move to parent 
class but if it find it in the class D then it wont go to the parent class which is C. 

'''

# Example 3

class F:                          # Parent class 
    
    def __init__(self):                      
        print('In init F')
        
    def clf(self):
        print('Class F')
    
        
class G():                        # parent class
    
    def __init__(self):                      
        print('In init G')
        
    def clg(self):
        print('Class G')


class H(F,G):                     # derived class
    def inH1(self):                      
        print('class H')
    
    def inH2():
        print('class H')

h1 = H()                           # It will print = In it F
    
    
