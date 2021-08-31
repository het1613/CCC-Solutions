def zero():
    for i in range(2):
        print(' *** ')
        for j in range(3):
            print('*'+' '*3+'*')
    print(' *** ')

def one():
    for i in range(2):
        for j in range(3):
            print(' '*3+'*')
        print()

def two():
    print(' *** ')
    for i in range(3):
        print(' '*4+'*')
    print(' *** ')
    for i in range(3):
        print('*')
    print(' *** ')

def three():
    for i in range(2):
        print(' *** ')
        for i in range(3):
            print(' '*4+'*')
    print(' *** ')

def four():
    for i in range(3):
        print('*'+' '*3+'*')
    print(' *** ')
    for i in range(3):
        print(' '*4+'*')

def five():
    print(' *** ')
    for i in range(3):
        print('*')
    print(' *** ')
    for i in range(3):
        print(' '*4+'*')
    print(' *** ')

def six():
    print(' *** ')
    for i in range(3):
        print('*')
    print(' *** ')
    for i in range(3):
        print('*'+' '*3+'*')
    print(' *** ')

def seven():
    print(' *** ')
    for i in range(2):
        for j in range(3):
            print(' '*4+'*')
        print()

def eight():
    for i in range(2):
        print(' *** ')
        for i in range(3):
            print('*'+' '*3+'*')
    print(' *** ')

def nine():
    print(' *** ')
    for i in range(3):
        print('*'+' '*3+'*')
    print(' *** ')
    for i in range(3):
        print(' '*4+'*')
    print(' *** ')

digit=int(input('Enter a digit between 0 and 9: '))

if (digit==0):
    zero()
    
if (digit==1):
    one()
    
if (digit==2):
    two()
    
if (digit==3):
    three()

if (digit==4):
    four()
    
if (digit==5):
    five()
    
if (digit==6):
    six()
    
if (digit==7):
    seven()

if (digit==8):
    eight()
    
if (digit==9):
    nine()

    
        
    
        

    
    
    
    
