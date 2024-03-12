# Basic dictionary operations


name = {'A101':'Ashok','A102':'John','A103':'Carol','A104':'Harry'}


# add,modify,delete
name['A106'] = 'Elvis'      # add new key-value pair

name['A102'] = 'Newton'     # modify value for key

del(name['A106'])           # delete a key-value pair

# del(name)                 # deletes the dictionaries object
# print(name)

# Dictionary Methods
'''
=> Two dictionaries cannot be concatenated using +.
=> Two dictionaries cannot be merged like a = b + c.
=> Two dictionaries cannot be compared using <,>.

'''
di = {'A101':'Ashok','A102':'John','A103':'Carol','A104':'Harry'}
dc = {10:'a',20:'b',30:'c'} 


print(di.get('A101','Not Present'))         # Prints value 'Ashok'
print(di.get('A105','Not Present'))         # Prints 'Not Present'

di.update(dc)                               # Updates dc with di items
print(di.pop(10))
dc.clear()                                  # Clears the dictionary

# A dictionary containing different keys but same values can be created using a fromkeys() function as shown below:
lst = [1,2,4,3,10]
d = dict.fromkeys(lst,'a')                  # prints {1: 'a', 2: 'a', 4: 'a', 3: 'a', 10: 'a'}
print(d)

# Dictionary Varieties
'''
keys in dictionary must be unique and immutable. Numbers, strings or tuples can be used as keys. If tuple is used as a key, 
it should not contain any mutable element like list.

''' 
contacts = {
    'Anil':{'DOB':'17/11/98','class':'C'},
    'john':{'DOB':'01/06/99','class':'D'},
    'Newton':{'DOB':'20/12/91','class':'A'}    
}

for k,v in contacts.items():
    print(k,'-->',v)