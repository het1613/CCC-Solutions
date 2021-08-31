def RomanToDecimal(roman):
    previous_value=999999999999
    total=0

    numerals=['I','V','X','L','C','D','M']
    values=[1,5,10,50,100,500,1000]

    for char in roman:
        pos=numerals.index(char)
        current_value=values[pos]
            
        if (current_value>previous_value):
            total+=current_value-(2*previous_value)
        else:
            total+=current_value

        previous_value=current_value

    return total


def DecimalToRoman(decimal):
    hundreds_numerals=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    tens_numerals=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    ones_numerals=['','I','II','III','IV','V','VI','VII','VIII','IX']

    roman=''

    hundreds=decimal//100
    decimal=decimal%100
    roman+=hundreds_numerals[hundreds]

    tens=decimal//10
    decimal=decimal%10
    roman+=tens_numerals[tens]

    ones=decimal
    roman+=ones_numerals[ones]

    return roman    


num_of_tests=int(input('Enter number of tests: '))

output=['\n']

for test in range(num_of_tests):
    line=input('Enter the expression: ')
    original=line

    line=line[:-1].split('+')

    num_1=line[0]
    num_2=line[1]

    answer=RomanToDecimal(num_1)+RomanToDecimal(num_2)

    if (answer>1000):
        result=original+'CONCORDIA CUM VERITATE'

    else:
        result=original+DecimalToRoman(answer)

    output.append(result)

print('\n\n'.join(output))
