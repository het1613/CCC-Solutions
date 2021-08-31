deck=[input() for card in range(52)]

print()

high_cards_name=['ace','king','queen','jack']
high_cards_value=[4,3,2,1]

player='A'

player_A_total=0
player_B_total=0

for pos in range(len(deck)):
    if (deck[pos] in high_cards_name):
        index=high_cards_name.index(deck[pos])

        if ((52-pos)>high_cards_value[index]):

            for iteration in range(pos+1,pos+1+high_cards_value[index]):
                if deck[iteration] in high_cards_name:
                    break

            else:
                points=high_cards_value[index]

                if (player=='A'):
                    player_A_total+=points
                else:
                    player_B_total+=points

                print('Player {0:s} scores {1:d} point(s).'.format(player,points))

    if (player=='A'):
        player='B'
    else:
        player='A'

print()
print('Player A: {0:d} point(s).'.format(player_A_total))
print('Player B: {0:d} point(s).'.format(player_B_total))
