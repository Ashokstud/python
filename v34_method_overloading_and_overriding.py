# method overloading
class meth:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            res = a+b+c
        elif a!=None and b!=None:
            res = a+b
        else:
            res = a
        print(res)

m1 = meth()
# m1.add(10,20)


# method overriding
class method1:
    def show(self):
        print('show method 1')

class method2(method1):
    def show(self):
        print('show method 2')    

ele = method2()
ele.show()                            # Here method 1 show() func is override with the method 2 show() func.