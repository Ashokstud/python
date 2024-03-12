# Sets
'''Sets are like lists, with an exception that they do not contain duplicate entries.'''
a = {20}                        # Set with one item
b = {'Ashok',25,123.45}         # set with multiple items
c = {11,11,11,11}               # Only one 11 gets stored

'''While storing an element in a set, it's hash value is computed using a hashingtechnique to determine where it should be stored i the set.'''
'''No matter in which order we insert the elements in a set, they get stored in the same order'''

s = {12,23,45,16}            # prints {16, 12, 45, 23}
t = {23,12,16,45}            # prints {16, 12, 45, 23}
u = {45,16,12,23}            # prints {16, 12, 45, 23}
'''here we can see the above statement is printing the same set for s,t and u'''


s1 = {'morning','afternoon','night'}        #works
s2 = {(1,2),(3,4),(4,5)}                    #works
# s3 = {[12,23],[15,23],[45,65]}              #Error
# since strings and tuples are immutable, their hash value remains same at all times. Hence a set of strings or tuples is permitted. Howevwer,
# a list may change, so its hash value may change, hence a set of list may change, so its hash value may change, hence a set of lists is not permitted.

# Set methods
d = {100,200,300,400,500,600,700,800,550,750}
e = {'A','B','C'}
f = {}


d.add(1000)                 # add value 1000 in in set d
d.update(e)                 # adds the set e in d
f = d.copy()                # set d copied in the f
d.remove(100)               # Remove 100 from set
# d.remove(101)             # throws error
d.discard(101)              # Won't throw the error but 101 is not in the set
d.discard(300)              # Remove 300 from the set
e.clear()                   # REmove all elements

set1 = {21,22,23,24,25,26,27,28,29,30}
set2 = {21,23,25,27}
print(set1.issuperset(set2))    #True
print(set1.issubset(set2))      #False
print(set1.isdisjoint(set2))    #False





