year=input("Please enter year you would like to check: ")
int(year)

if year%4==0:
    if year%100==0 and year%400!=0:
        isLeapYear = False
    else:
        isLeapYear = True
else:
    isLeapYear = False

if isLeapYear is True:
    print ("This year {} is leap year.".format(year))
else:
    print ("This year {} is not leap year.".format(year))
