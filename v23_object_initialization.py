# Object initialization
'''
There are two ways to initialize an object:
Method 1 >> Using methods like get_data()/set_data()
Method 2 >> Using special method __init__()

'''
class employee:
    def getdata(self,n,a):
        self.name = n
        self.age = a
        
    def display(self):
        print(self.name,self.age)


e1 = employee()
e1.getdata('Name',10)
e1.display()


class student():
    def __init__(self,n,a):                                 # __init__() method is always called when object is created.
        self.naam = n
        self.saal = a
    
    def display(self):
        print('Student name =',self.naam,'\nage =',self.saal)


s1 = student('ash',10)
s1.display()
