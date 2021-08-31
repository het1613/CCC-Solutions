keypad=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

outputs=[]

num_of_tests=int(input('Enter number of tests: '))

for test in range(num_of_tests):
    old_number=input('Enter phone number: ').replace('-','')

    converted_number=''

    for char in old_number:

        digit=char

        if (char.isalpha()):
            for group in keypad:
                if (char in group):
                    digit=str(keypad.index(group)+2)

        converted_number+=digit

    converted_number=converted_number[:3]+'-'+converted_number[3:6]+'-'+converted_number[6:10]

    outputs.append(converted_number)

print('\n'.join(outputs))
            
