snakes_and_ladders=[[9,34],[40,64],[67,86],[54,19],[90,48],[99,74]]

position=1

while position<100:
    dice_sum=eval(input('\nEnter total sum of dice: '))

    position+=dice_sum

    if (dice_sum==0):
        print('You Quit')
        break

    for current_snake_ladder in snakes_and_ladders:
        if (position==current_snake_ladder[0]):
            position=current_snake_ladder[1]

    if (position>100):
        position-=dice_sum

    print('You are now on square',position)
    
else:
    
    print('\nYou Win')
