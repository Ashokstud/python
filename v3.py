# This is the program for reveerseing the string and printing it in capital format.

str = "Hi there!"
str1 = "HI"
l = len(str)
t=1
char = ''
while l>0:
    l-=1
    char+=str[-t]
    t+=1
print(char)
print(str.upper())
