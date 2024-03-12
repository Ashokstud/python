# Repetition control instruction 

# While loop
'''
x = int(input('Enter the value of x: '))
while x==5:
    print("Welcome!")
    x=1
'''
'''
s = 'Mumbai vihar'
tpl = (10,20,30,40,50,60,11)
lst = ['hi','hello','how','are','you','dear','bear']         #index of tpl and list have to be same.
i = 0
while i<len(lst):
    print(i,s[i],tpl[i],lst[i])
    i+=1
'''   

# For loop 
'''
tpl = (10,20,30,40,50,60,11)
for var in tpl:
    print(var,end=' ')          # end=' ' is used to avoid printing values in newline.
'''

# program for finding if its a prime number
'''
num = int(input('Enter the number: '))
n = 2
while n<num:
    if num%n==0:
        print(num,"is not prime number")
        break                                   # Break is used to terminte the loop and come out of it immediately
    n+=1
else:
    print("It's a prime number")
'''

# Program for finding the number is multiple of 10 or not
'''
tpl = (10,20,30,40,50,60,11)
for var in tpl:
    if var%10!=0:
        print(var,'Is not multiple of 10')
    else:
        print(var,'Is multiple of 10')
'''

# Program to convert from binary to decimal
binc = str(input('Enter the number: '))
flag = True
for var in binc:
    if var == '0' or var=='1':
        flag = True
    else:
        flag = False
if flag==True:
    l = len(binc)
    dec = 0
    i = 0
    b = -1
    while i<l:
        dec = dec + (int(binc[b])*2**i)
        b-=1
        i+=1
    print(dec)
else:
    print('Incorrect binary code!')
