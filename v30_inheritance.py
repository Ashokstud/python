# Inheritance 
'''
>> In inheritance a new class called derived class can be created to inherit features of an existing class called base class.
>> Base class is also called super class or parent class.
>> Derived class is also called sub class or child class.

''' 
# Single level inheritance

class A:                           # super class a
    def cl1(self):
        print('Class A')
    
        
class B(A):                        # Derived class/Sub class
    def cl2(self):
        print('Class B')

b2 = B()
# b2.cl2()
# b2.cl1()
'''
class A
>> cl1

class B
>>cl1
>>cl2

'''

# Multilevel Inheritence

class C:
    def in1(self):                      # Super class
        print('class C')
    
    def in2(self):
        print('class C')

class D(C):                             # parent class/ sub class(derived)
    def in3(self):
        print('class D')
    
    def in4(self):
        print('class D')

class E(D):                             # child class/ sub class(derived)
    def in5(self):
        print('class E')
    def in6(self):
        print('Class E')

e1 = E()
# e1.in1()


# multiple inheritance

class F:                          # Parent class 
    def clf(self):
        print('Class F')
    
        
class G():                        # parent class
    def clg(self):
        print('Class G')


class H(F,G):                     # derived class
    def inH1(self):                      
        print('class H')
    
    def inH2():
        print('class H')

h1 = H()
h1.clf()
h1.clg()