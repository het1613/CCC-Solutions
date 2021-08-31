height=int(input('Enter height: '))

stars=1
space=(height-1)*2

star_multiplier=1
space_multiplier=-1

for iteration in range(height):
    line='*'*stars+' '*space+'*'*stars

    if (stars==height):
        star_multiplier=-1
        space_multiplier=1

    stars+=(2*star_multiplier)
    space+=(4*space_multiplier)

    print(line)
