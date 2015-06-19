year1=input("Please enter year you would like to check: ")
year=int(year1)


if year%4==0:
        isLeapYear=not(year%100==0 and year%400!=0)
else:
    isLeapYear = False


def leapYearPrint(str):
	print str;
    

if isLeapYear:
    leapYearPrint(str="This year {} is leap year.".format(year1))
else:
    leapYearPrint(str="This year {} is not leap year.".format(year1))
