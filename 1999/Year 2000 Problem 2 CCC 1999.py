def letter_or_digit(char):
    if (char.isdigit()) or (char.isalpha()):
        return True
    else:
        return False

def format_A(pos,line):
    if (pos>0 and letter_or_digit(line[pos-1])):
        pass

    elif (pos+8<len(line) and  letter_or_digit(line[pos+8])):
        pass

    elif (pos+7>=len(line)):
        pass

    else:
        day=line[pos:pos+2]
        month=line[pos+3:pos+5]
        year=line[pos+6:pos+8]

        if (day.isnumeric() and int(day)>=1 and int(day)<=31) and \
           (month.isnumeric() and int(month)>=1 and int(month)<=12) and \
           (year.isnumeric() and int(year)>=0 and int(year)<=99) and \
           (line[pos+2]=='/' and line[pos+5]=='/'):

            if (int(year)<25):
                line=line[:pos+6]+'20'+line[pos+6:]
            else:
                line=line[:pos+6]+'19'+line[pos+6:]

    return line

def format_B(pos,line):
    if (pos>0 and letter_or_digit(line[pos-1])):
        pass

    elif (pos+8<len(line) and  letter_or_digit(line[pos+8])):
        pass

    elif (pos+7>=len(line)):
        pass

    else:
        year=line[pos:pos+2]
        month=line[pos+3:pos+5]
        day=line[pos+6:pos+8]

        if (day.isnumeric() and int(day)>=1 and int(day)<=31) and\
           (month.isnumeric() and int(month)>=1 and int(month)<=12) and\
           (year.isnumeric() and int(year)>=0 and int(year)<=99) and\
           (line[pos+2]=='.') and (line[pos+5]=='.'):

            if (int(year)<25):
                line=line[:pos]+'20'+line[pos:]

            else:
                line=line[:pos]+'19'+line[pos:]

    return line

def format_C(pos,line):
    if (pos>0 and letter_or_digit(line[pos-1])):
        pass

    else:
        months=['January','February','March','April','May','June','July','August','September','October','Novermber','December']

        for month in months:
            length=len(month)

            if (pos+length<len(line) and line[pos:pos+length]==month):
                pos=pos+length
                break

        else:
            pos=9999999999999999

        if (pos+7<len(line) and letter_or_digit(line[pos+7])):
            pass

        elif (pos+6>=len(line)):
            pass

        else:
            day=line[pos+1:pos+3]
            year=line[pos+5:pos+7]
            comma_1=line[pos+3:pos+5]
            comma_2=line[pos]

            if (day.isnumeric() and int(day)>=1 and int(day)<=31) and\
               (year.isnumeric() and int(year)>=0 and int(year)<=99) and\
               (comma_1==', ' and comma_2==' '):

                if (int(year)<25):
                    line=line[:pos+5]+'20'+line[pos+5:]

                else:
                    line=line[:pos+5]+'19'+line[pos+5:]
    return line


num_of_lines=int(input())

outputs=['\n']

for iteration in range(num_of_lines):
    line=input()
    pos=0

    while (pos<len(line)):
        line = format_A(pos,line)
        line = format_B(pos,line)
        line = format_C(pos,line)
        pos+=1

    outputs.append(line)

print('\n'.join(outputs))
