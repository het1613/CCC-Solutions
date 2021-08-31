keyword=input('Enter the keyword: ')
text=input('Enter text: ')

punctuation="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "+'"'

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in punctuation:
    text=text.replace(char,'')

text=text.upper()

groups=[]

while (len(text)>0):
    groups.append(text[:len(keyword)])

    text=text[len(keyword):]

encoded_text='\n'

for current_group in groups:

    for keyword_pos in range(len(keyword)):
    
        if (len(current_group)>keyword_pos):

            shift=alphabet.index(keyword[keyword_pos])
            
            new_char_index=alphabet.index(current_group[keyword_pos])+shift

            new_char_index%=26

            new_char=alphabet[new_char_index]

            encoded_text+=new_char

print(encoded_text)

    

    
