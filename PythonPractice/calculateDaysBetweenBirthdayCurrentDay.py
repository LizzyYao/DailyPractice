#during my study, I am trying to get a better understanding on how return, def, variable assignment work together under a stucture of a bigger program.
#this is one of the challenges in my coding study.
#this practice is actually a copy of the instructor's example code from the Udacity course "Intro to Computer Science", instructor: Dave Evans
def isLeapYear(year):
	if year%400==0:
		return True
	if year%100==0:
		return False
	if year%4==0:
		return True
	return False
	
def daysInMonth(year, month):
	if month==1or month==3 or month==5 or month ==7 or month=8 or month==10 or month==12:
		return 31
	else:
		if month==2:
			if isLeapYear(year):
				return 29
			return 28
		else:
			return 30

def nextDay(year,month,day):
	if day<daysInMonth(year,month):
		return year, month, day+1
	else:
		if month<12:
			return year, month+1, 1
		else:
			return year+1,1,1
			
def dateIsBefore(year1,month1,day1,year2,month2,day2):
	if year1<year2:
		return True
	if year1==year2:
		if month1<month2:
			return True
		if month1==month2:
			return day1<day2
	return False


def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	days=0
	#here the instructor have an assert clause. I haven't got it yet. copy here. "assert not dayIsBefore(year2,month2,day2,year1,month1,day1)"
	#assume the value are all valid.
	while dateIsBefore(year1,month1,day1,year2,month2,day2):
		year1,month1,day1=nextDay(year1,month1,day1)
		days=days+1
	return days

daysBetweenDates(1906,3,12,2015,10,11)

