'''
for num in [1,2,3,4,5,6]:
    print(num)
    
for ch in 'good morning':
    print(ch)

# Both these for loops call __iter__() method of list/str. This method returns an iterator object. The iterator object has a 
# method __next__() which returns the next item in the list/str container.

'''


'''
lst = [1,2,3,4,5]
l = lst.__iter__()
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
'''

# User defined iterators
'''
Suppose we wish our class to behave like an iterator. To do this we need to define __iter__() and __next__() in it.

'''
class avjd:
    def __init__(self,data):
        self.__data = data
        self.__len = len(data)
        self.__first = 0
        self.__sec = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__sec == self.__len:
            raise StopIteration
        self.__avg = (self.__data[self.__first]+self.__data[self.__sec])/2
        self.__first += 1 
        self.__sec += 1
        return self.__avg
    
lst = [10,20,30,70,50]
d = avjd(lst)
for val in d:
    print(val)
            