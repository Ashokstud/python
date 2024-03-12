# Write the python program to carry out the following operations:
'''
=> Add an ! at the end of the tuple
=> Convert a tuple to to a string 
=> Extract ('b','b') from the tuple
=> Find out number of 'e' in the tuple 
=> check whether 'r' exists in the tuple
=> convert the tuple to a list
=> Delete characters 'b','b','e','r' from the tuple
'''

tpl = ('F','l','a','b','b','e','r','g','a','s','t','e','d')

# addition of ! is not possible as the tuple is immutable
# So to add ! we need to create a new tuple and then make tpl refer to it

tpl = tpl + ('!',)
print(tpl)

s = ''.join(tpl)
print(s)

t = tpl[3:5]
print(t)

c = tpl.count('e')
print(c)

if 'r' in tpl:
    print('Available')

lst = list(tpl)
print(lst)

tpl = tpl[:3]+tpl[7:]
print(tpl)