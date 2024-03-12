def ssort(lst):
    l = len(lst)
    for i in range(l):
        min = i
        for j in range(i,l):
            if lst[min]>lst[j]:
                min = j
        
        lst[i],lst[min] = lst[min],lst[i]
    return lst

lst = [5,1,4,2,3,70,9,10]
slst = ssort(lst)
print(slst)



def bsearch(lst,n):
    l = len(lst)
    f = 0
    l = l-1
    while (f<=l):
        m = (f+l)//2
        if lst[m] == n:
            print('found at:',m)
            return 0
        else:
            if n < lst[m]:
                l = m-1
            else:
                f = m+1
    print('Not Found')   
        
        

bsearch(lst,n=70)