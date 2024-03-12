'''
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if 0 < new_age <= 120:  # A simple age validation
            self.__age = new_age
        else:
            print("Invalid age!")

# Creating an instance of the Student class
student1 = Student("Alice", 20)

# Accessing data through member functions
print(f"Initial name: {student1.get_name()}")
print(f"Initial age: {student1.get_age()}")

# Modifying data through member functions
student1.set_name("Bob")
student1.set_age(22)

# Accessing modified data
print(f"Updated name: {student1.get_name()}")
print(f"Updated age: {student1.get_age()}")

# Attempting to access data directly would raise an AttributeError
# For example:
print(student1._Student__name)  # This would result in an AttributeError

'''
'''
class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, num):
        self.__result += num
        print(f"Added {num}. Result: {self.__result}")

    def get_result(self):
        return self.__result

# Creating an instance of the Calculator class
calculator = Calculator()

# Adding numbers using the add method
calculator.add(5)
calculator.add(10)
calculator.add(7)

# Getting the final result
final_result = calculator.get_result()
print(f"Final result: {final_result}")

'''

# a = 20
# b= 20
# i = a
# j = i
# j = 10

# print(id(a),id(i),id(j),id(b))

class meth:
    def __init__(self,n='ash',a=0):
        self.__name = n
        self.__age = a
        self.ag = a
    def display(self):
        print(self.__name,self.__age,self.ag)
    def method(a=0,b=0):
        print('method',a+b)
    def method():
        print('hello')

# m1 = meth()
# meth.method(10,20)
# m1.display()

# class A:
#     def __init__(self,val):
#         self.value = val
#         self.__ab = 20
#         print(self.value)
    
#     def show(self):
#         print(self.__ab)
         
# a = A(10)
# print(a.value)
# a.show()


# class hi:
#     def fun1(self):
#         print('Hello')

# h1 = hi()


# Linear search
# pos = -1
# def search(lst,n):
    
#     for var in lst:
#         globals()['pos']+=1
#         if var==n:
#             return True
        
#     return False    

# lst = [12,34,56,78,23,46,123,12]
# n = int(input('Enter number: '))
# if search(lst,n):
#     print('found at position:',pos+1)
# else:
#     print('Not found')

