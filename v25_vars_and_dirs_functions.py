# vars() and dir() functions
'''
>> vars() returns a dictionary of attributes and their values.
>> dir() returns a list of attributes.

'''

class employee:
    
    var = 'cycle'               # This var variable is the class namespace(variable) it is common for all objects not for any particular object.
    
    def __init__(self,n = '',a = 0):
        self.name = n           # This name variable is the instance namespace(variable)                      
        self.age = a
        
    def display(self):
        print(self.name,self.age)
        
e1 = employee()      
print(vars(e1))
print(dir(e1))
# print(dir(employee))