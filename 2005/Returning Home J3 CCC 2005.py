directions=[]

while True:
    instruction=input()
    
    if instruction=='SCHOOL':
        break
    
    directions.append(instruction)

directions=directions[::-1]

for pos in range(0,len(directions)-1,2):
    if (directions[pos]=='R'):
        turn='LEFT'
    else:
        turn='RIGHT'

    street=directions[pos+1]

    print('Turn %s onto %s street.' %(turn,street))

if (directions[-1]=='R'):
    turn='LEFT'
else:
    turn='RIGHT'

print('Turn %s on into your HOME.' %(turn))
