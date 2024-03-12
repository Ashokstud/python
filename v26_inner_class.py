
class student():
    def __init__(self,n,a):                                 # __init__() method is always called when object is created.
        self.naam = n
        self.saal = a
    
    def display(self):
        print('Student name =',self.naam,'\nage =',self.saal)
        self.lap = self.laptop()           # creating the object inside method for the belonging object(s1).
        self.lap.show()
        
        
    class laptop:
        def __init__(self):
            self.brand = 'Asus'
            self.ram = '8GB'
            self.processor = 'AMD Ryzen 3550H'
        def show(self):
            print(self.brand,self.ram,self.processor)

s1 = student('Ashok',23)
s1.display()

# or

lap1 = student.laptop()                     # for creating the object for inner class we havve to use the parent class. But if we dont use it it will not be created.
lap1.show()

