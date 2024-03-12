# Bubble sort
def bsort(lst):
    l = len(lst)
    for j in range(l-1):
        for i in range(l-1):
            if lst[i]>lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
        l -= 1
    return lst
           
        
    
    
lst = [5,4,3,2,1]
sort = bsort(lst)
print(sort)




# Palindrome 
'''
def rev(str):
    strrev = ''
    l = len(str)
    for val in range(1,l+1):
        strrev+=str[-val]
    return strrev

str ='pap'
strrev= rev(str)
if str == strrev:
    print('Palindrome')
    
else:
    print('not palindrome')
'''

