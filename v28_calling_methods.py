# Calling functions and methods 

def printit():                          # Global function
    print('Opener')

class message:
    def display(self,msg):              # instance method
        printit()
        print(msg)
        
    def show():                         # Class method
        printit()
        print('Hello')


printit()

m = message()   
m.display('Good day')                   # Call instance method
# m.show()                              # it throws error because you can call only instance method through object. 
message.show()                          # Call Class method