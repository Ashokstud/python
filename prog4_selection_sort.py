# Selection Sort

def ssort(lst):
    l = len(lst)
    for i in range(l):
        min = i
        for j in range(i,l):
            if lst[j] < lst[min]:
                min = j
        
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp
   
    return lst
           
        
    
    
lst = [1, 8, 2, 7, 3, 6, 4, 5, 10, 9]
sort = ssort(lst)
print(sort)
        
        
    