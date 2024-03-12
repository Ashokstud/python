'''
>> It is a good idea to keep data in a class inaccessible from outside the class and acces it through memberfunctions of the 
   class only.
>> Example: __name,__age,__sal,etc.

if you have a class named MyClass with an instance variable __variable, Python will internally change it to _MyClass__variable. 
This modification helps to prevent unintentional name collisions, as the mangled name becomes more unique.

'''
class MyClass:
    def __init__(self):
        self.__variable = 42

obj = MyClass()
# Accessing the variable directly will result in an AttributeError
# because the name has been mangled.
# print(obj.__variable)  # This would raise an AttributeError

# Instead, you should use the mangled name
print(obj._MyClass__variable)  # This will print 42
