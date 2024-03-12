# Program for Stack

size = int(input('Enter the Size of stack: '))
stack=[]
print('Enter the operation you like to perform:\n=>Enter 1 for push\n=>Enter 0 for pop\n')
choice = int(input('Enter your choice here: '))
flag = 1
i = 0
if choice == 1:
    while flag==1 and i<size:
        num = int(input('\n\n\nEnter the number: '))
        stack.append(num)
        a=int(input('Enter 1 to continue and 0 to exit: '))
        if a == 1:
            flag = a
        elif a == 0:
            flag = a
        else:
            print('Invalid Input!\n\n\n\n')
            print('Last attempt Left!\n\n')
            a=int(input('Enter 1 to continue and 0 to exit: '))
            if a == 1:
                flag = a
            elif a == 0:
                flag = a
           
        if flag == 0:
            break 
        i+=1
        if i >= size:
            print('\n\nOverflow!')

choice = int(input('\n\nDo you want to perform Pop operation if yes press 0 if no press 1: '))
    
if choice == 0:
    if not stack:
        print('\n\nStack is Underflow')
        flag = 0
    while(flag):
        print('\n\n\nYou deleted the element',stack[-1])
        stack.pop()
        d=int(input('\nEnter 1 to continue and 0 to exit: '))
        flag = d

dec = int(input('\n\n\nIf you want to display the Stack (Enter 1)\nIf you do not want to display the Stack (Enter 2)\nYour input: ') )
if dec==1:
    if not stack:
        print('\n\nStack is Empty')
    else:
        print('\n\n\n')
        print(stack)
else:
    print('Thank you')