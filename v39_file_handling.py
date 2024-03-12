# File Types 
'''
>> All program files are text files
>> All image, music, video, executable files are binary files.

'''

# File I/O
'''
# Sequence of operation in file I/O
    - Open a file
    - Read/Write data to it
    - close the file

'''
# Write/Read text data
msg1 = 'How to get girls\n'
msg2 = 'always start your with "How you doing?"\n'
msg3 = 'Dont\'t feel bad\n'
msg4 = 'if you don\'t get girls....\n'
f = open('demo','w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.write(msg4)
f.close()

r = open('demo','r')
data = r.read()
print(data)
r.close()
