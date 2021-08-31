def ahead(steps):
    print(1)
    print(abs(steps))


num_of_cases=int(input())

for case in range(num_of_cases):
    direction=0
    x_coordinate=0
    y_coordinate=0

    while True:
        change=int(input())

        if (change==0):
            break

        if (change==1):
            steps=int(input())

            if (direction==0):
                x_coordinate+=steps

            elif (direction==90):
                y_coordinate+=steps

            elif (direction==180):
                x_coordinate-=steps

            elif (direction==270):
                y_coordinate-=steps

        elif (change==2):
            direction-=90

            if (direction<0):
                direction=270

        elif (change==3):
            direction+=90

            if (direction>=360):
                direction=0

    distance=abs(x_coordinate)+abs(y_coordinate)

    print()
    print('Distance is',distance) 

    if y_coordinate > 0 and x_coordinate > 0 and direction==0:
        print(2)
        ahead (y_coordinate)
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate > 0 and x_coordinate > 0 and direction==90:
        print(3)
        ahead (x_coordinate)
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate > 0 and direction==180: 
        ahead (x_coordinate)
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate > 0 and direction==270:
        ahead (y_coordinate)
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate > 0 and x_coordinate < 0 and direction==0:
        ahead (x_coordinate)
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate < 0 and direction==90:
        print(2)
        ahead (x_coordinate)
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate < 0 and direction==180:
        print(3)
        ahead (y_coordinate)
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate > 0 and x_coordinate < 0 and direction==270:
        ahead (y_coordinate)
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate < 0 and direction==0:
        ahead (x_coordinate)
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate < 0 and x_coordinate < 0 and direction==90:
        ahead (y_coordinate)
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate < 0 and direction==180:
        print(2)
        ahead (y_coordinate)
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate < 0 and direction==270:
        print(3)
        ahead (x_coordinate)
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate < 0 and x_coordinate > 0 and direction==0:
        print(3)
        ahead (y_coordinate)
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate > 0 and direction==90:
        ahead (y_coordinate)
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate > 0 and direction==180:
        ahead (x_coordinate)
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate < 0 and x_coordinate > 0 and direction==270:
        print(2)
        ahead (x_coordinate)
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate==0 and x_coordinate > 0 and direction==0:
        print(2)
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate==0 and x_coordinate > 0 and direction==90:
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate==0 and x_coordinate > 0 and direction==180:
        ahead (x_coordinate)
        
    elif y_coordinate==0 and x_coordinate > 0 and direction==270:
        print(2)
        ahead (x_coordinate)
        
    elif y_coordinate > 0 and x_coordinate==0 and direction==0:
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate==0 and direction==90:
        print(3)
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate==0 and direction==180:
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate==0 and direction==270:
        ahead (y_coordinate)
        
    elif y_coordinate==0 and x_coordinate < 0 and direction==0:
        ahead (x_coordinate)
        
    elif y_coordinate==0 and x_coordinate < 0 and direction==90:
        print(2)
        ahead (x_coordinate)
    elif y_coordinate==0 and x_coordinate < 0 and direction==180:
        print(3)
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate==0 and x_coordinate < 0 and direction==270:
        print(3)
        ahead (x_coordinate)
        
    elif y_coordinate < 0 and x_coordinate==0 and direction==0:
        print(3)
        ahead (y_coordinate)
        
    elif y_coordinate < 0 and x_coordinate==0 and direction==90:
        ahead (y_coordinate)
        
    elif y_coordinate < 0 and x_coordinate==0 and direction==180:
        print(2)
        ahead (y_coordinate)
        
    elif y_coordinate > 0 and x_coordinate==0 and direction==270:
        print(3)
        print(3)
        ahead (y_coordinate)
    




