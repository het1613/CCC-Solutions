#Top Yodeller S2 CCC 2004
#Het Patel
#ICS4U0
#9/22/20

#I kept input empty so I can copy past input info quickly to test program
#But for final code I would have ask the user for the input
user_input=input().split() #gets input and makes into list, splitting at white spaces

num_of_contestants=int(user_input[0]) #assigning variable to each element
num_of_rounds=int(user_input[1])

all_scores=[0 for contestant in range(num_of_contestants)] #creates empty list of to keep track of scores for all contestants
worst_rank=[0 for contestant in range(num_of_contestants)] #creates empty list of to keep track of worst ranks for all contestants

for current_round in range(num_of_rounds): #for loop which goes through all contest rounds

    current_scores=[int(score) for score in input().split()] #gets the scores for all contestants, makes into
                                                             #list splitting at white spaces, makes all elements
                                                             #integer values and appends to current_scores list

    for contestant in range(num_of_contestants): #for loop which goes through all the scores of the contestants
        all_scores[contestant]+=current_scores[contestant] #adds the current score of contestant in the round to
                                                           #the sum of all scores of contestant from previous rounds

    sorted_current_scores=sorted(current_scores)[::-1] #sorts the current_score list in accending order, then reverses
                                                       #the list and assigns new vaibale to this sorted list

    for contestant in range(num_of_contestants): #for loop which goes through all the worst ranks of the contestants
        score_rank=sorted_current_scores.index(current_scores[contestant])+1 #finds the rank of each contestant in the
                                                                             #depending on their score in the current rank
        
        if worst_rank[contestant]<score_rank: #checks if the contestant has a worst rank from previous rounds
            worst_rank[contestant]=score_rank #if they don't, the rank from this round becomes their worst rank

#creates a 2D list of all contestants with their contestant number, total score and their worst rank
all_data=[[contestant+1,all_scores[contestant],worst_rank[contestant]] for contestant in range(num_of_contestants)]

#sorts all_data by score in accending order (key=lambda x:x[1]), then reverses it to sort score by decending order.
#If score is the same for 2 or more contestants, it then sorts by contestant number accending order
all_data=sorted(all_data, key=lambda x:x[1], reverse=True)

#print(all_data) #for error checking

pos=0 #creates variable to keep track of the position of the highest scoring contestant

flag=True #creates boolean variable to continue printing for multiple winners

print() #prints empty line

while flag: #create while loop to keep printing TopYoddeller if flag is True
    contestant_number=all_data[pos][0] #gets contestant number of contestant with highest score
    score=all_data[pos][1] #gets score of contestant with highest score
    worst_rank=all_data[pos][2] #gets worst rank of contestant with highest score

    #prints the winner
    print('Yodeller {} is the TopYodeller: score {}, worst rank {}'.format(contestant_number,score,worst_rank))

    pos+=1 #moves onto next highest scoring contestant

    #checks if score of next contestant is the same as the winner
    #if it is, flag stays True, else it becomes False and while loop broken
    flag=(pos<num_of_contestants) and (score==all_data[pos][1])          
        

    
        
