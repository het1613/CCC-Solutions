def dictionary_coding(text):

    new_text=[]
    
    for word in text:

        if (word not in dictionary):
            dictionary.append(word)
            new_text.append(word)

        else:
            new_text.append(str(dictionary.index(word)+1))

    new_text=' '.join(new_text)

    return new_text


global dictionary

num_of_tests=int(input())

print()

all_outputs=[]

for test in range(num_of_tests):

    dictionary=[]

    test_output=''

    while True:

        text=input()

        if (text==''):
            break
        
        text=text.split()

        new=dictionary_coding(text)

        test_output+=new+'\n'

    all_outputs.append(test_output)

print('\n'.join(all_outputs))

    
