outputs=[]

num_of_words=int(input('Enter number of words: '))

for iteration in range(num_of_words):
    word=input('Enter word: ')

    all_substrings=[]

    for start in range(len(word)):
        for end in range(len(word)+1):
            substring=word[start:end]

            if (substring not in all_substrings):
                all_substrings.append(substring)

    outputs.append(str(len(all_substrings)))

print('\n'.join(outputs))
