#to get the year from user input and convert string to integer.
def userInputYear():
        year=raw_input("Please enter a year you would like to check: ")
        year=int(year)
        return year


#evaluate input year is leap year or not.
def checkLeapYear():
    if year%4!=0 or (year%100==0 and year%400!=0):
        return False    
    else:
        return True
		

#print evaluation result: is or not leap year.
def printLeapYearResult():
	if LeapYear is True:
		print ("This year {} is leap year.".format(year))
	else:
		print("This year {} is not a leap year.".format(year))

year=userInputYear()
LeapYear=checkLeapYear()
printLeapYearResult()  
