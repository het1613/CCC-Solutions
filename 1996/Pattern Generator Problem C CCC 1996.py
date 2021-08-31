num_of_tests=int(input())

all_outputs=[]

for test in range(num_of_tests):

    test_output=['The bit patterns are:']
    
    user_input=input().split()

    length=int(user_input[0])
    ones=int(user_input[1])

    pattern='1'*ones+'0'*(length-ones)

    test_output.append(pattern)

    print(pattern)

    while True:
        
        if ('10' not in pattern):
            break

        for pos in range(len(pattern)-1,0,-1):
            if (pattern[pos-1]+pattern[pos]=='10'):
                break

        pattern=pattern[:pos-1]+'01'+(pattern[pos+1:])[::-1]

        print(pattern)

        test_output.append(pattern)

    test_output='\n'.join(test_output)

    all_outputs.append(test_output)

print()
print('\n\n'.join(all_outputs))

    
