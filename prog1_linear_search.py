# Linear search
pos = -1
t = False
def search(lst,n): 
    loc = []
    for var in lst:
        globals()['pos']+=1
        if var==n:
            globals()['t'] = True
            loc += [globals()['pos']+1]
    return loc
      

lst = [12,34,56,78,23,46,123,12]
n = int(input('Enter number: '))
loc = search(lst,n)
if t:
    if len(loc)>1:
        print('found at positions:',*loc)
    else:
        print('found at position:',*loc)
else:
    print('Not found')
    


# Linear search(easy)
'''
pos = -1
def search(lst,n):
    
    for var in lst:
        globals()['pos']+=1
        if var==n:
            return True
        
    return False    

lst = [12,34,56,78,23,46,123,12]
n = int(input('Enter number: '))
if search(lst,n):
    print('found at position:',pos+1)
else:
    print('Not found')
'''