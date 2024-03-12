# Dcumentation strings
def display():
    '''Display message'''
    print('Hello')
    print(display.__doc__)
    
def show(ms1 ='',ms2 = ''):
    '''
    Display 2 messages
    Arguments:
    msg1: message to display in lowercase
    msg2: messgae to display in uppercase
    
    '''
    print(ms1.upper())
    print(ms2.lower())
    
# display()
# show('paris','delhi')
# help(display)
# help(show)

'''
>> Using help() method we can print the functions/class/method documentation systematically.
>> The docstring is available in the attribute __doc__ of a module, function, class or method.

'''



import sys
print('number of arguments received =',len(sys.argv))
