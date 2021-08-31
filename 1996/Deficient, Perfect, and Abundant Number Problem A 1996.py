def isPerfect(number):
    counter=1
    factors_sum=0

    while (counter<number):
        if (number%counter==0):
            factors_sum+=counter

        counter+=1

    if (factors_sum==number):
        status='{0:d} is a perfect number.'.format(number)
        
    elif (factors_sum<number):
        status='{0:d} is a deficient number.'.format(number)

    else:
        status='{0:d} is an abundant number.'.format(number)

    return status


num_of_tests=int(input('Enter number of tests: '))

all_outputs=[]

for test in range(num_of_tests):

    number=int(input('Enter an integer: '))

    status=isPerfect(number)

    all_outputs.append(status)

print()

print('\n\n'.join(all_outputs))

    

    
