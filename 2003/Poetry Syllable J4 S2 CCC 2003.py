vowels='aeiou'

outputs=['\n']

num_of_verses=int(input())

for current_verse in range(num_of_verses):

    last_syllables=[]

    for line in range(4):
        
        last_word=((input().lower()).split())[-1]

        pos=-1

        syllable=''

        while (len(syllable)<len(last_word)):

            last_letter=last_word[pos]

            syllable+=last_letter

            if (last_letter in vowels):
                break

            pos-=1

        last_syllables.append(syllable)

    if (last_syllables[0]==last_syllables[1]==last_syllables[2]==last_syllables[3]):
        status='perfect rhyme'

    elif (last_syllables[0]==last_syllables[1]) and (last_syllables[2]==last_syllables[3]):
        status='even rhyme'

    elif (last_syllables[0]==last_syllables[2]) and (last_syllables[1]==last_syllables[3]):
        status='cross rhyme'
        
    elif (last_syllables[0]==last_syllables[3]) and (last_syllables[1]==last_syllables[2]):
        status='shell rhyme'

    else:
        status='free rhyme'

    outputs.append(status)

print('\n'.join(outputs))
            
            

    
