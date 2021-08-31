outputs=[]

boundary=input('Enter boundaries: ').split()

boundary_x=int(boundary[0])
boundary_y=int(boundary[1])

current_x=0
current_y=0

change=input('Enter new change in cursor: ').split()

while (change!=['0','0']):
    
    change_x=int(change[0])
    change_y=int(change[1])

    new_x=current_x+change_x
    new_y=current_y+change_y

    if (new_x<0):
        new_x=0

    if (new_x>boundary_x):
        new_x=boundary_x

    if (new_y<0):
        new_y=0

    if (new_y>boundary_y):
        new_y=boundary_y

    new_coordinates=str(new_x)+' '+str(new_y)

    outputs.append(new_coordinates)

    current_x=new_x
    current_y=new_y

    change=input('Enter new change in cursor: ').split()

print('\n'.join(outputs))
