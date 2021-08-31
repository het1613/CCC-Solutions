current_year=int(input('Enter the current year: '))
future_year=int(input('Enter a future year: '))

for year in range(current_year,future_year+1,60): #LCM of 4,2,3,5 is 60 so every
                                                  #60 years, new government elected
    print('All positions change in year',year)
