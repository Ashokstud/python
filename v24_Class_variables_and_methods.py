# Variables and methods

# namespace is the name assigned to the object and method/function.


class employee:
    
    var = 'cycle'               # This var variable is the class namespace(variable) it is common for all objects not for any particular object.
    
    def getdata(self,n,a):
        self.name = n           # This name variable is the instance namespace(variable)                      
        self.age = a
        
    def display(self):
        print(self.name,self.age)


e1 = employee()
e1.getdata('John',23)
e1.display()
print(e1.var)                    # Object can use the var variable but it can no modify the var variable for class variable
employee.var = 'Bus'             # Only using class varaible we can change the value.
print(employee.var)