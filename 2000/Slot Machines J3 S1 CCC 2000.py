quarters=int(input('Enter number of quarters: '))
first=int(input('Enter how many times first machine has been played: '))
second=int(input('Enter how many times second machine has been played: '))
third=int(input('Enter how many times third machine has been played: '))

counter=0

while (quarters>0):
    first+=1
    
    second+=1
    
    third+=1
    
    quarters-=3
    
    if (first==35):
        quarters+=30
        first=0

    if (second==100):
        quarters+=60
        second=0
   
    if (third==10):
        quarters+=9
        third=0

    counter+=3

print('\nMartha plays {0:d} times before going broke.'.format(counter))
