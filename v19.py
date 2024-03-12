# Recursive Function
'''A python function can be called from within its body. When we do so it is called a recursive function'''
'''
def rfun(n):
    if n == 0:
        return 1
    else:
        p = n * rfun(n-1)
    return p

num = int(input('Enter the number: '))
fact = rfun(num)
print('factorial value =',fact)
'''

# Types of Recursion
'''
>> Head recursion
>> Tail recursion

'''

# Head recursion - In this type of recursion the recursive call is made before other processing in the function.
def headprint(n):
    if n == 0:
        return
    else:
        headprint(n-1)
        print(n)
        
# headprint(10)

# Tail recursion - In this type of recursion processing is done before the recursive call.
# The tail recursion is similar to a loop - the function executes all the statements before making the recursive call.

def tailprint(n):
    if n == 0:
        return
    else:
        print(n)
        tailprint(n-1)

# tailprint(10)
