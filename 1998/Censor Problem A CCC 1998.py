num_of_sentences=int(input('Enter number of sentences: '))
outputs=[]

for iteration in range(num_of_sentences):
    sentence=input('Enter sentence: ').split()
    new=[]
    
    for word in sentence:
        if (len(word)==4):
            new.append('****')
        else:
            new.append(word)

    new=' '.join(new)
    
    outputs.append(new)

print('\n'.join(outputs))
