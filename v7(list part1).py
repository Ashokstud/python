# Container
'''Definition'''
# Container is an entity which contains multiple data items. It is also known as collection or a compound data type.

# Python has following container data types:
'''Lists'''
'''Tuples'''
'''Sets'''
'''Dictionaries'''

#List

'''A list is defined by writing comma-seperated elements within []'''
num = [10,20,30,40,50,60]
names = ['ashok','robert','john','jesse','martha']

# list can contain dissimilar types, though
# Usually they are a collection of similar types.
data = ['ashok',10,90.5]

naam = ['ashok','robert','john','jesse','martha']

# Mutability
'''Unlike Strings, lists are mutable (changeable). So, lists can be updated as shown below:'''

naam1 = ['ashok','robert','john','jesse','martha']
naam1[1] = 'changed'
print(naam1)

# Concatenation
naam2 = ['ashok','robert','john','jesse','martha']
naam2 = naam2 + ['add1','add2','add3']
print(naam2)

# merging
naam3 = ['C1ashok','C1robert']
naam4 = ['C2john','C2jesse','C2martha']
merge = naam3 + naam4
print(merge)

# Conversion
'''A string/tuple/set can be converted into a list using the list() conversion function'''
str1 = 'Ashok'
lst1 = list(str1)
print(lst1)

# Searching
naam5 = ['ashok','robert','john','jesse','martha']
search = 'ashok' in naam5
print(search)

