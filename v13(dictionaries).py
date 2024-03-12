#Dictionaries
'''Dictionary is a collection of key-value pairs'''
'''Dictionaries are also known as maps or associative arrays'''

d1 = {}
d2 = {'A101':'Ashok','A102':'John','A103':'Carol','A104':'Harry'}

# Here, 'A101', 'A102', 'A103' & 'A104' are keys, Whereas, 'Ashok', 'john', etc are values.

# Conditions
'''
=> Different keys may have same values.
    d = {10:'a',20:'a',30:'c'}              # ok


=> Keys must be unique. If keys are same, but values are different, latest key value pair gets stored.
    d = {10:'a',20:'b',10:'c'}              # will store {10:'c',20:'b'}


=> if key value pairs are repeated, then only pair gets stored
    d = {10:'a',20:'b',10:'a'}              # will store {10:'a',20:'b'}
'''

di = {'A101':'Ashok','A102':'John','A103':'Carol','A104':'Harry'}
print(di['A101'])

# Looping in dictionaries
courses = {'DAA':'CS','AOA':'ME','SVY':'CE'}

# Iterate over key-value pairs
for k,v in courses.items():
    print(k,v)

# Iterate over keys
for k in courses.keys():
    print(k)
    
# Iterate over keys in shorter way
for k in courses:
    print(k)
    
# Iterate over values
for v in courses.values():
    print(v)
    
    
# enumerate used to keep track of index.   
for i,(k,v) in enumerate(courses.items()):
    print(i,k,v)
