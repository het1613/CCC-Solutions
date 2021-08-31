num_of_tests=int(input())

outputs=[]

for test in range(num_of_tests):
    dividend=int(input())
    original_divisor=int(input())

    current_divisor=original_divisor

    quotient=0

    if (dividend>=current_divisor):

        quotient=''
        
        extra_zeros=len(str(dividend))-len(str(original_divisor))

        current_divisor=original_divisor*(10**extra_zeros)

        while (dividend<=current_divisor):
            current_divisor=current_divisor//10

        while (dividend>=original_divisor):

            zeros=0
            
            while (dividend<=current_divisor):
                current_divisor=current_divisor//10
                zeros+=1

            quotient+='0'*zeros

            counter=0

            while (current_divisor<=dividend):
                counter+=1
                dividend-=current_divisor

            current_divisor=current_divisor//10

            quotient+=str(counter)

    outputs.append(str(quotient))
    outputs.append(str(dividend))
    outputs.append('')

print()
print('\n'.join(outputs))
    
