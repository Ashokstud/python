# identity 
'''
naam1 = ['ashok','robert','john','jesse','martha']
naam2 = ['ashok','robert','john','jesse','martha']
print(naam1 is naam2)                               #False

naam3 = naam1
print(naam3 is naam1)                               #True

print(naam1 is not naam2)                           #True
'''

# Comparision
'''
Comparision is done item by item till there is a mismatch. In the following code it would be decided 
that A is less than B when 2 and 6 are compared.
'''
A = [1,2,3,4]
B = [1,6,3,4]
# print(A<B)


# Emptiness 

lst = []
# if not lst:
    # print('Empty List')

# Using Built-in functions on list
'''

num = int(input('Enter the number: '))
if num in number:
    print('The location is: ',number.index(num))
else:
    print('Sorry!',num,'is not in List')
'''
number = [10,100,20,90,30,80,40,70,50,60]
del(number[0])      #delete the number at 0
del(number[2:5])    #delete the number from 2 to 4
# print(number)

number1 = [10,100,20,90,30,80,40,70,50,60]
number1.append(110)       #add number1 at the end (at most 1 argument)
number1.remove(70)        #remove 10 from the number1 (at most 1 argument)
# number1.remove(0)       #throws error that 0 isn't in number1 (at most 1 argument)
number1.pop()             #removes last item from the list number1 (at most 1 argument)
number1.pop(2)            #removes the item at loc 2. (at most 1 argument)
a = number1.index(100)    #it show the loc of 100

# print(number1)

#Sorting And reversing 

number2 = [10,100,20,90,30,80,40,70,50,60]
# number2 = ['ashok','robert','john','jesse','martha']
number2.sort()          #sort the list     [Note: the original list is modified]
number2.reverse()       #reverse the list  [Note: the original list is modified]

number3 = [10,100,20,90,30,80,40,70,50,60]
print(list(reversed(number3)))  #prints the reversed list but dont make any changes to the original list
print(sorted(number3))          #prints the sorted list but dont make any changes to the original list
print(number3)                  #It will print the original list as nothing changes from the above functions.