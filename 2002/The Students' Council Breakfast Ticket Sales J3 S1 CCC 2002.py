#Programmer: Het Patel
#Date Written: 11/11/19
#Version: C_2
#Purpose: display all the possible combination of ticket sales that will result in required money, total number of combinations and minimum number of tickets that must be printed. 

from math import ceil

#Getting all inputs
price_pink=int(input('Cost of PINK tickets: ')) 
price_green=int(input('Cost of GREEN tickets: '))
price_red=int(input('Cost of RED tickets: '))
price_orange=int(input('Cost of ORANGE tickets: '))
total_sales=int(input('How much must be raised with ticket sales?: '))

counter=0 #Keeps count of how many combinations there are
minimum_print=99999 #Keeps count of the minimum prints required

print('\nComboinations are')

for pink_amount in range(ceil(total_sales/price_pink)+1): #Goes through a 4-nested loop to find all combinations that add up to required amount

    for green_amount in range(ceil(total_sales/price_green)+1):

        for red_amount in range(ceil(total_sales/price_red)+1):

            for orange_amount in range(ceil(total_sales/price_orange)+1):
                current_combo_sales=(pink_amount*price_pink)+(green_amount*price_green)+(red_amount*price_red)+(orange_amount*price_orange) #This is the current sales with the current combination

                if (current_combo_sales==total_sales):
                    print('# of PINK is %-3s # of GREEN is %-3s # of RED is %-3s # of ORANGE is %s' %(pink_amount,green_amount,red_amount,orange_amount)) #Prints out combination if it matches with required sales
                    counter+=1
                    combo_min=pink_amount+green_amount+red_amount+orange_amount

                    if (combo_min<minimum_print): #Checks if a new minimum print is created and if so, new minimum print is added
                        minimum_print=combo_min

#Prints out number of combinations and minimum number of tickets to print
print('Total Combinations is {}.'.format(counter)) 
print('Minimum number of tickets to print is {}.'.format(minimum_print))
