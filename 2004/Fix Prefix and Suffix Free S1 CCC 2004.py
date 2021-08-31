num_of_collections=int(input('Enter the number of collections: '))

outputs=[]

for collection in range(num_of_collections):
    words=[input('Enter word: ') for i in range(3)]

    status='Yes'

    for pos_1 in range(len(words)):
        
        for pos_2 in range(len(words)):
            
            if (pos_1!=pos_2) and (status=='Yes'):
                
                if (words[pos_1].startswith(words[pos_2])) or (words[pos_1].endswith(words[pos_2])):

                    status='No'

                    break

    outputs.append(status)

print('\n'.join(outputs))
                
