from abc import ABC,abstractmethod           # abc is module stand for abstract base classes, from abc we have imported ABC class and decorator abstractmethod 

class method(ABC):                 # the class which contain abstract method is called as abstract class.
    @abstractmethod                # we need to mark met() as abstract method using the decorator @abstractmethod
    def met(self):
        pass
    
class student(method):       # derived class   # we can use student class only if we will use the method name same as the abstract method of abstract class
    def metho(self):
        print('Hello 1')

# s1 = student()        # ERROR # as the class is inheriting the features of the abstract class without defining a method name same as the abstract method, so it throws error


class teacher(method):
    def met(self):
        print('Hello 2') 
    
    def process():
        print('Hey!')

# m1 = method()            #ERROR # the class which contain abstract method we cannot make its instance.

s2 = teacher()
s2.met()
teacher.process()