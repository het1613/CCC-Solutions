tine_length=int(input('Enter tine length:\n'))
tine_space=int(input('Enter tine spacing:\n'))
handle_height=int(input('Enter handle height:\n'))

tine_line='*'+' '*tine_space+'*'+' '*tine_space+'*'

handle_base='*'*tine_space*2+'***'

handle=' '*(tine_space+1)+'*'

for line in range(tine_length):
    print(tine_line)

print(handle_base)

for line in range(handle_height):
    print(handle)
