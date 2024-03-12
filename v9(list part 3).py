# nested lists  (It's kind a like 2D array)

a = [1,3,4,8]
b = [2,6,9,5]
c = [a,b]
print(c[1][3],c[0][2])    #prints the element from the row(1) and coloumn(3) which is '5' and row(0) and coloumn(2) which is '4'.

# Embedded list 
a = [1,3,4,8]
b = [2,6,9,a,5]
print(b)                  # it prints [2, 6, 9, [1, 3, 4, 8], 5]



c = [1,3,4,8]
d = [2,6,9,*c,5]          # [Note: * operator unpacks the list]
print(d)                  # it prints [2, 6, 9, 1, 3, 4, 8, 5] . Here, 1,3,4,8 are unpacked.