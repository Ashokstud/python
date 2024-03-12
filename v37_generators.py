# Generators
'''
>> Generators are very efficient functions that create iterators. they use yield statement instead of return whenever they wish 
   to return data from the function.
   
>> Speciality of the generator is that, it remembers the state of the function and the last statement it had executed when yield 
   was executed.

'''
def gen(dat):
    for i in range(0,len(dat)):
        yield(dat[i]) 

lst = [6,7,8,4,5]
l = gen(lst)
for i in l:
    print(i,end=' ')