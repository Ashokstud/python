# Operator Overloading

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        sum = student(m1,m2)
        sum = m1+m2
        return sum
s1 = student(10,20)
s2 = student(30,40)

s4 = s1 + s2
print(s4)

        
