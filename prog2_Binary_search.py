def bsearch(lis,n):
    r = len(lis)
    l = 0
    u = r-1
    while l<=u:
        mid = (l+u)//2
        
        if lis[mid]==n:
            print('Found at position:',mid)
            return
        else:
            if lis[mid]<n:
                l = mid + 1  
            else: 
                u = mid -1
    print('Not found')
        
    


lis = [10,12,23,45,76,89,90,105,256,512]
n = int(input('Enter the number: '))
bsearch(lis,n)