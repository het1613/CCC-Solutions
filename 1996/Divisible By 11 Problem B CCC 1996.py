num_of_tests=int(input('Enter number of tests: '))

all_outputs=[]

for test in range(num_of_tests):

    test_output=[]

    number=int(input('Enter an integer: '))
    original=number

    test_output.append(str(number))

    last_digit=number%10
    number=(number//10)-last_digit

    while (number>=11):
        test_output.append(str(number))
        
        last_digit=number%10
        number=(number//10)-last_digit

    status='The number {0:d} is not divisible by 11.'.format(original)

    if (number==11):
        status='The number {0:d} is divisible by 11.'.format(original)

    test_output.append(status)
    test_output='\n'.join(test_output)
    all_outputs.append(test_output)

print()
print('\n\n'.join(all_outputs))

        

    
