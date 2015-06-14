year=int(input("Please enter year you would like to check: "))
if year%4==0:
	if year%100==0 and year%400!=0:
		leapYear="not leap year"
	else:
		leapYear="leap year"
else:
	leapYear="not leap year"
print ("This year {} is {}".format(year,leapYear)), 