year=int(input("Please enter year you would like to check: "))
if year%4==0:
	if year%100==0 and year%400!=0:
		print ("This year {} is not leap year.".format(year))
	else:
		print ("This year {} is leap year.".format(year))
else:
	print ("This year {} is not leap year.".format(year))