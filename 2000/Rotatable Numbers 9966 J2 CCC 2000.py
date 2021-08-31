start=int(input('Enter start: '))
end=int(input('Enter end: '))

print()

rotatable_digits=['1','6','8','9','0']

counter=0

for iteration in range(start,end+1):
    flag=True

    num=str(iteration)

    for digit in num:
        if digit not in rotatable_digits:
            flag=False
            break
        
    reversed_num=num[::-1]

    new_num=''

    if flag:
        for digit in reversed_num:
            
            if digit in '180':
                new_num+=digit
                
            elif digit=='6':
                new_num+='9'
                
            elif digit=='9':
                new_num+='6'

        if (new_num==num):
            counter+=1
            print(num)

print('\nThe number of rotatable numbers is:')
print(counter)
