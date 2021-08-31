num_of_tests=int(input())

all_outputs=[]

for test in range(num_of_tests):

    test_output=[]
    
    undeafeated=int(input())

    test_output.append('\n')

    one_loss=0
    eliminated=0
    counter=0

    while True:
        if ((undeafeated==0) and (one_loss==1)):
            break
        
        test_output.append('Round {0:d}: {1:d} undefeated, {2:d} one-loss, {3:d} eliminated'.format(counter,undeafeated,one_loss,eliminated))

        if ((undeafeated==1) and (one_loss==1)):
            undeafeated=0
            one_loss=2
            
        else:
            eliminated+=int(one_loss//2)
            one_loss+=int((undeafeated//2) - (one_loss//2))
            undeafeated-=int(undeafeated//2)

            print(undeafeated,one_loss)
        
        counter+=1

    test_output.append('Round {0:d}: {1:d} undefeated, {2:d} one-loss, {3:d} eliminated'.format(counter,undeafeated,one_loss,eliminated))
    test_output.append('There are {0:d} rounds'.format(counter))
    test_output.append('\n')

    all_outputs.append('\n'.join(test_output))

print('\n'.join(all_outputs))
        

    
    
