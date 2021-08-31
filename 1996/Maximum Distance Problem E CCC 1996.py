num_of_tests=int(input())

all_outputs=[]

for test in range(num_of_tests):
    length=int(input())
    seq_1=[int(digit) for digit in input().split()]
    seq_2=[int(digit) for digit in input().split()]

    max_distance=0

    for pos_1 in range(length):
        
        for pos_2 in range(length-1,-1,-1):

            if (seq_1[pos_1]<=seq_2[pos_2]) and (pos_1<=pos_2):

                current_distance=pos_2-pos_1

                if (current_distance>max_distance):
                    max_distance=current_distance

    test_output='The maximum distance is {0:d}'.format(max_distance)

    all_outputs.append(test_output)

print()
print('\n\n'.join(all_outputs))
