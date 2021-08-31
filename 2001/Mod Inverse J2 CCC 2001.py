#Programmer: Het Patel
#Date Written: 9/23/20
#Version: 1.0
#Purpose: To find the modular inverse of a given integer, x, in relation to another given integer, m.

x=int(input('Enter x: ')) #Getting all inputs
m=int(input('Enter m: '))

for num in range(1,m): #Going in a loop until the right modulo inverse is found
    product=x*num
    
    if (product%m==1):
        status='\nInverse of {} modulo {} is: {}'.format(x,m,num) #Printing out the correct modulo inverse and breaking out of loop
        break
else:
    status='\nInverse of {} modulo {} is: No such integer exists'.format(x,m) #If program did not break, no integer is found

print(status)
