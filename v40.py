# Read/Write operations
'''
msg = '2024 elections ere going to be the biggest in the history, as half of the world population will be voting.\n'
msgs = ['How\n','you\n','doing?\n']
f = open('demo','w')
f.write(msg)
f.writelines(msgs)

tpl = ('ajay',23,15000,)
st = {23,45,67,78,90,12,}
d = {'name':'Borat','age':25}
f.write(str(tpl))
f.write(str(st))
f.write(str(d))
'''

# readline
'''
f = open('demo','r')
while True:
    data = f.readline()
    if data == '':
        break
    print(data,end='')
'''  
    
# or
'''
f = open('demo','r')
for data in f:
    print(data,end='')
'''  
# Moving within a file 
'''
>> At times we may wish to move to desired position in a file before read/write. this can be done using seek() method.
>> reference can take values 0,1,2,... it makes that reference as starting position/ current position.
'''

r = open('temp','r')
r.seek(4)
print(r.readline())
