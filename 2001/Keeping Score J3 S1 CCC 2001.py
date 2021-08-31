seq=input('Enter cards: \n')

all_values=[0,0,0,0]

all_faces=[[],[],[],[]]

current='C'

for char in seq:
    if (char in 'DHS'):
        current=char

    if (char not in 'CDHS'):
        if (char in 'JQKA'):
            value='JQKA'.index(char)+1
            
        else:
            value=0
        
        if (current in 'CDHS'):
            pos='CDHS'.index(current)
            all_faces[pos].append(char)
            all_values[pos]+=value

for index in range(4):
    if (len(all_faces[index])==0):
        all_values[index]+=3

    elif (len(all_faces[index])==1):
        all_values[index]+=2

    elif (len(all_faces[index])==2):
        all_values[index]+=1

total=sum(all_values)

clubs_value=all_values[0]
clubs_face=all_faces[0]

diamonds_value=all_values[1]
diamonds_face=all_faces[1]

hearts_value=all_values[2]
hearts_face=all_faces[2]

spades_value=all_values[3]
spades_face=all_faces[3]

print('\n%-25s%s' %('Cards Dealt','Points'))
print('%s %-22s%s' %('Clubs',' '.join(clubs_face),clubs_value))
print('%s %-19s%s' %('Diamonds',' '.join(diamonds_face),diamonds_value))
print('%s %-21s%s' %('Hearts',' '.join(hearts_face),hearts_value))
print('%s %-21s%s' %('Spades',' '.join(spades_face),spades_value))
print('%26s %s' %('Total',total))



