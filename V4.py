#  logical operators: Complex decision making can be done using logical operators "and, or and not".

a = 40
b = 30

# 'and' operator evaluates ALL expressions. It returns last expresssions evaluate to True. 
# Otherwise, it returns first value that evaluates to false.
''' 
x = 75 and a>=20 and b<60 and 35    # Here all the expression are True so the last expression is the O/P which is 35
y = a>30 and b>40                   # Here in this line the first statement which is False is (b>40) then it will be the O/P is False
z = a>30 and 0 and b>40 and 10      # Here in this line the first statement which is False is 0 then it will be the O/P is 0
print(x)
print(y)
print(z)

'''
# 'or' operator evaluates all expressions and returns the first value that evaluates to true. 
#  Otnerwise, it returns last value that evaluate to False.
'''
x = 75 or a>=40 or 60       # first value that is true is '75' so O/P is also 75
y = a<20 or 0               # Last value that is false is 0 so O/P is also 0
z = a<20 or False or 1000   # the first value that is True is 1000 so O/P is 1000.
print(x)
print(y)
print(z)

'''



# Conditional Expression 
'''
age = 60 
status = 'minor' if age<18 else 'adult'                                  #This will show 'Adult'
print(status)

# Nested conditional operator

status = 'Minor' if age<18 else 'Adult' if age<60 else 'Senior Citizen'  #This will show 'Senior citizen'
print(status)
'''

# Receiving Input
# input() function used to receive input values from the keyboard
'''
age = int(input('Enter the age: '))
salary = float(input('Enter the salary: '))
print(age,salary)

'''
