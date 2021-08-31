start=int(input('Start value: '))
end=int(input('End value: '))

grid=[['  ' for i in range(11)] for j in range(11)]

row=5
col=5
steps=0
pos=start

while (pos<end):
    steps+=1

    #down
    counter=1
    while (counter<=steps) and (pos<=end):
        grid[row][col]='%02d'%(pos)
        row+=1
        pos+=1
        counter+=1

    #right
    counter=1
    while (counter<=steps) and (pos<=end):
        grid[row][col]='%02d'%(pos)
        col+=1
        pos+=1
        counter+=1

    steps+=1
        
    #up
    counter=1
    while (counter<=steps) and (pos<=end):
        grid[row][col]='%02d'%(pos)
        row-=1
        pos+=1
        counter+=1
        
    #left
    counter=1
    while (counter<=steps) and (pos<=end):
        grid[row][col]='%02d'%(pos)
        col-=1
        pos+=1
        counter+=1

for row in grid:
    print(' '.join(row))

    
