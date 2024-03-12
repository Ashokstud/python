'''Variable names, function names and class names are in general called identifiers'''

# Namespaces
'''
>> As the name suggests, a namespace is a space that holds names(identifiers).
>> An identifier used in a function or a method belongs to the Local namespace.
>> An identifier used outside a function or a method belongs to the global namespace.
 
'''
'''
def fun():
    # name conflict. local a shadows out global a
    a = 45
    # name conflict, use global b
    global b       # it helps in modifying the global value
    b = 6.28
    
    # uses local a, global b and s
    # no need to define s as global, since it is not being changed
    print(a,b,s)
    
# global identifiers
a = 20
b = 3.14
s = 'abra ka dabra'
fun()
print(a,b,s)    
'''

# Inner function
'''Outer functions'''
def display():
    a = 500
    print('saving is the best thing...')
    
    '''inner function'''
    def show():
        print('honesty is the worst policy')
        print(a)
    show()
    
def fun():
    display()

fun()



    
 

