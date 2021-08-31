outputs=[]

word=input('Enter a word: ')

while (word!='X'):
    while True:
        if ('ANA' in word):
            word=word.replace('ANA','A')
            
        elif ('BAS' in word):
            word=word.replace('BAS','A')
            
        else:
            break

    status='NO'

    if (word=='A'):
        status='YES'

    outputs.append(status)

    word=input('Enter a word: ')

print('\n'.join(outputs))
