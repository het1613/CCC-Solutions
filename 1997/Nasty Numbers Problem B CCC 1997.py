def NastyNumber(num):

    factor_limit=round(num**0.5)+2

    factors=[]

    for factor_1 in range(1,factor_limit):
        if (num%factor_1==0):
            factor_2=int(num/factor_1)
            factors.append([factor_1,factor_2])
        
    for pair_1 in factors:
        for pair_2 in factors:
            if (abs(pair_1[0]-pair_1[1])==pair_2[0]+pair_2[1]):
                return True

    return False

num_of_tests=int(input('Enter number of tests: '))

outputs=[]

for test in range(num_of_tests):
    num=int(input('Enter number: '))

    status='{0:d} is not nasty'.format(num)
    
    if NastyNumber(num):
        status='{0:d} is nasty'.format(num)

    outputs.append(status)

print()
print('\n'.join(outputs))
