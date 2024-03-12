# Tuples
'''
=> Though a list can store dissimilar data but it's generally used to store similar data.

=> As opposite to the list tuple can store similar data but usually used to the storing of the similar data.

'''
tpl = ('aShok',25,3.14)

# Mutability
'''Unlike a list, a tuple is immutable, i.e., it cannot be modified'''
tpl1 = ('aShok',25,3.14)
# tpl1[0] = 'matt'           #it throws error as tuple doesn't support assignment

# Tuple variety 
'''
It is all same as the list
[Note: *operator is used to unpack a tuple same as lists]
'''

# basic operation 
'''
the other basic operations that are done on a tuple are very similar to the one one on a list.
> Concatenation 
> Merging
> Conversion
> Searching
> Identity
> Comparision 
> Emptiness
'''
# isinstance() is used to check whether a instance of which type.

lst = ['ashok','john','kevin',('shane','jordan'),'jarvis']
tpl = ('ashok','john','kevin',['shane','jordan'])
c,d=0,0
for var in tpl:
    if isinstance(var,tuple):                      #isinstance check whether the var is tuple or not
        c+=1
    else:
        d+=1
print(c,'\n',d)