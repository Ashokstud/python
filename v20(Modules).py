# Modules and packages
'''The main module'''
'''A module is a .py file containing definition and statements. So, all .py files that we created so far for our programs are modules.'''
'''when we execute a program its module name is __main__. This name is available in the variable __name__.'''
print(__name__) 
from math import sqrt
import random
print(random.randint(1,20))
print(sqrt(25))

