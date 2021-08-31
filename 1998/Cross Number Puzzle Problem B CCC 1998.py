#Question 1:
def isPerfect(number):
    counter=1
    factors_sum=0

    while (counter<number):
        if (number%counter==0):
            factors_sum+=counter

        counter+=1

    if (number==factors_sum):
        return True
    else:
        return False

print('Question 1 (Perfect Integers): ')

for number in range(1000,10000):
    if isPerfect(number):
        print(number)

print()


#Question 2:
def cubes_sum(number):
    sum_of_digits=0

    for digit in number:
        sum_of_digits+=int(digit)**3

    return sum_of_digits

print('Question 2(Cubes Sum): ')

for number in range(100,1000):
    if (cubes_sum(str(number))==number):
        print(number)
