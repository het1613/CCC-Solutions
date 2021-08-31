#Programmer: Het Patel
#Date Written: 9/22/20
#Version: 1.0
#Purpose: To output the Canadian version of an American-spelt word

vowels='aeiouy'

while True:
    word=input('\nEnter a word: ').lower()

    if (word=='quit!'):
        break

    if (len(word)>4):
        pos=0
        
        while (pos<len(word)-1):

            print(word[pos])
            
            if (word[pos]+word[pos+1]=='or'):
                consonant_pos=pos-1

                if (word[consonant_pos] not in vowels):
                    word=word.replace('or','our',1)
                    pos+=1
                    
            pos+=1
            
    print(word)
