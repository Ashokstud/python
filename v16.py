# Comprehension
'''Comprehensions offer an essay and compact way of creating lists, sets and dictionaries'''

# List comprehension 
'''lst = [expression for var in sequence]'''

import random
lst = [random.randint(10,100) for n in range(20)]
lst1 = [(x,x**2,x**3) for x in range(10)]
# print(lst)                   # o/p = [38, 91, 42, 46, 78, 15, 22, 40, 42, 13, 15, 29, 97, 27, 14, 95, 27, 56, 73, 18]       
# print(lst1)                  # o/p = [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]

# Set Comprehension
'''s = {expression for var in sequence}'''

a = {10,20,30,40,50,60}
num = {x for x in a if x<20 or x>50}
print(num)                                 # o/p = {10,60}



# Dictionaries Comprehension
'''dic = {key:value for (key,value) in dictionary.items()}'''
d = {'a':1,'b':2,'c':3,'d':4}

d1 = {k:v**3 for(k,v) in d.items()}
print(d1)


