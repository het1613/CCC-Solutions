num_of_adjectives=int(input('Enter number of adjectives: '))
num_of_nouns=int(input('Enter number of nouns: '))

all_adjectives=[input() for adjective in range(num_of_adjectives)]
all_nouns=[input() for noun in range(num_of_nouns)]

all_phrases=[]

for adjective in all_adjectives:
    for noun in all_nouns:
        phrase=adjective+' as '+noun

        all_phrases.append(phrase)

print('\n'.join(all_phrases))
    

