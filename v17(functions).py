# Functions
'''Python function is a block of code that performs a specific and well defined task'''
'''
# function definition
def f1():
    print('first function')

f1()
f1()
'''


# Types of arguments
# arguments are of 4 types:
'''
>> Positional Arguments 
>> Keyword Arguments
>> Variable-length positional arguments
>> Variable-length keyword arguments

'''


'''
# Positional arguments 
# must be passed in correct positional order
def fun1(i,j,k):
    print(i+j)
    print(k.upper())
    
fun1(10,3.14,'dhokla')              # Correct call
# fun1('cat',10,12.23)              # Error, incorrect order
'''

# Keyword arguments
# can be passed out of order. Python interpreter uses keywords (variable names) to match the values passed with the arguments used in the function definition.
'''
def fun2(it,a,str):
    print(it,a,str)
    
# fun2(10,a = 3.14,str='NJP')
fun2(a = 3.14,str='NJP',it=10)      # correct call
fun2('Ashu',1,34)                   # correct call
# fun2(p=1,q=2.12,r='BGD')            # Error, as the keyword name doesn't match.
'''

# Variable length positional arguments
# Variable length positional arguments can be received using *args
'''args used in definition of tup() is a tuple. * indicates that it will hold all the arguments passed to tup(). The tuple can be iterated through using a for loop'''
def tup(*args):       
    print(args)
    print(type(args))


tup(10,20,30,40)
tup(10,3.14,'hi')


# Variable length keyward arguments
# Variable length positional arguments can be received using *args
'''kargs used in definition of dic() is a dictionary. * indicates that it will hold all the arguments passed to dic(). The dictionary can be iterated through using a for loop'''
def dic(**kargs):       
    print(kargs)
    print(type(kargs))

dic(a=10,b=20,c=30,d=40)

