start=int(input('Enter day: '))
days=int(input('Enter the number of days in the month: '))
week=['','','','','','','']

print('%-4s%-4s%-4s%-4s%-4s%-4s%s' %('Sun','Mon','Tue','Wed','Thr','Fri','Sat'))
week[start-1]=1

day=start
total_days=2

while total_days<=days:
    week[day]=total_days
    day+=1
    total_days+=1
    
    if (day==7):
        print('%-4s%-4s%-4s%-4s%-4s%-4s%s' %(week[0],week[1],week[2],week[3],week[4],week[5],week[6]))
        week=['','','','','','','']
        day=0

print('%-4s%-4s%-4s%-4s%-4s%-4s%s' %(week[0],week[1],week[2],week[3],week[4],week[5],week[6]))
    
    
