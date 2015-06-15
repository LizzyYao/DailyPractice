number=input("Please enter a number: ")
int(number)

if number==0:
	print("0 is neither odd number nor even number.")
else:
	if number%2==0:
		evenNumber=True
	else:
		evenNumber=False
#output
if evenNumber is True:
	print("{} is a even number".format(number))
else:
	print("{} is a odd number".format(number))
	
