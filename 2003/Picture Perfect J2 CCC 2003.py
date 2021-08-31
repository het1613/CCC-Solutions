while True:
    num=int(input('\nEnter number of pictures: '))

    if (num==0):
        break
    
    min_perimeter=999999

    dimentions=''

    for length in range(1,num+1):
        
        for width in range(1,num+1):
            
            if (length*width==num):

                perimeter=2*(length+width)
                
                if (perimeter<min_perimeter):
                    
                    min_perimeter=perimeter
                    
                    dimentions=str(length)+' x '+str(width)
                    
    print('Minimum perimeter is {} with dimensions {}'.format(perimeter, dimentions))
    
    
                    
