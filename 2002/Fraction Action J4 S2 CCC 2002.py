def GreatestCommonDenominator(num1,num2):
    for divisor in range(num1,1,-1):
        if ((num1%divisor==0) and (num2%divisor==0)):
            return divisor
    return 1

numerator=int(input('Numerator: '))
denominator=int(input('Denominator: '))

GCD=GreatestCommonDenominator(numerator,denominator)

numerator=int(numerator/GCD)
denominator=int(denominator/GCD)

whole_number=numerator//denominator
remainder=numerator%denominator

print()

if (numerator>=denominator):
    print(str(whole_number),end=' ')

if (remainder>0):
    print('{:d}/{:d}'.format(remainder,denominator))
