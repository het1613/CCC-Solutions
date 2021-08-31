width=int(input())
hieght=int(input())
corner_width=int(input())
corner_hieght=int(input())
total_steps=int(input())

squares=[[True for column in range(width)] for row in range(hieght)]

for row in range(1,hieght+1):
    for column in range(1,width+1):

        if ((row<=corner_hieght and (column<=corner_width or column>width-corner_width))) or \
            (row>hieght-corner_hieght and (column<=corner_width or column>width-corner_width)):

            squares[row-1][column-1]=False

current_column=corner_width
current_row=0

direction=0

for step in range(total_steps):
    squares[current_row][current_column]=False

    if (direction==0):
        if (current_row-1>=0) and (squares[current_row-1][current_column]):
            current_row-=1
            direction=90

        elif (current_column+1<width) and (squares[current_row][current_column+1]):
            current_column+=1
            direction=0

        elif (current_row+1<hieght) and (squares[current_row+1][current_column]):
            current_row+=1
            direction=270

        elif (current_column-1>=0) and (squares[current_row][current_column-1]):
            current_column-=1
            direction=180

        else:
            break

    elif (direction==90):
        if (current_column-1>=0) and (squares[current_row][current_column-1]):
            current_column-=1
            direction=180

        elif (current_row-1>=0) and (squares[current_row-1][current_column]):
            current_row-=1
            direction=90

        elif (current_column+1<width) and (squares[current_row][current_column+1]):
            current_column+=1
            direction=0

        elif (current_row+1<hieght) and (squares[current_row+1][current_column]):
            current_row+=1
            direction=270

        else:
            break

    elif (direction==180):
        if (current_row+1<hieght) and (squares[current_row+1][current_column]):
            current_row+=1
            direction=270

        elif (current_column-1>=0) and (squares[current_row][current_column-1]):
            current_column-=1
            direction=180

        elif (current_row-1>=0) and (squares[current_row-1][current_column]):
            current_row-=1
            direction=90

        elif (current_column+1<width) and (squares[current_row][current_column+1]):
            current_column+=1
            direction=0

        else:
            break

    elif (direction==270):
        if (current_column+1<width) and (squares[current_row][current_column+1]):
            current_column+=1
            direction=0

        elif (current_row+1<hieght) and (squares[current_row+1][current_column]):
            current_row+=1
            direction=270

        elif (current_column-1>=0) and (squares[current_row][current_column-1]):
            current_column-=1
            direction=180

        elif (current_row-1>=0) and (squares[current_row-1][current_column]):
            current_row-=1
            direction=90

        else:
            break

print()
print(current_column+1)
print(current_row+1)

            
