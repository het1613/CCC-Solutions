start=eval(input('Enter lower limit of range:\n'))
end=eval(input('Enter upper limit of range:\n'))

RSA_count=0

for number in range(start,end+1):
    
    divisor_count=0
    
    for divisor in range(1, number+1):
        
        if (number%divisor==0):
            divisor_count+=1
            
    if (divisor_count==4):
        RSA_count+=1

print('\nThe number of RSA numbers between {} and {} is {}'.format(start,end,RSA_count))
