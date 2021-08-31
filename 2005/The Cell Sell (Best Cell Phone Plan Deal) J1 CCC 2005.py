daytime_min=int(input('Number of daytime minutes?\n'))
evening_min=int(input('Number of evening minutes?\n'))
weekend_min=int(input('Number of weekend minutes?\n'))

daytime_min_A=daytime_min-100

if (daytime_min_A<0):
    daytime_min_A=0


daytime_min_B=daytime_min-250

if (daytime_min_B<0):
    daytime_min_B=0

plan_A_cost=round((daytime_min_A*0.25)+(evening_min*0.15)+(weekend_min*0.2),2)
plan_B_cost=round((daytime_min_B*0.45)+(evening_min*0.35)+(weekend_min*0.25),2)

if (plan_A_cost>plan_B_cost):
    status='Plan B is cheapest.'
    
elif (plan_A_cost<plan_B_cost):
    status='Plan A is cheapest.'
    
else:
    status='Plan A and B are the same price.'

print('Plan A costs ${}'.format(plan_A_cost))
print('Plan B costs ${}'.format(plan_B_cost))
print(status)

