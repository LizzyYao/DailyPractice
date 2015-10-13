

#find largest number in 5 numbers.


#"get the numbers from user and convert string to float numbers."
def getFirstNumber():		
	firstNumber=raw_input("please enter your number: ")
	return float(firstNumber)


def compareNumberToFirstOne():
	largestNumber=getFirstNumber()
	x=1
	while x<5:
		numbers=raw_input("please enter your number: ")
		number2=float(numbers)
		if number2>largestNumber:
			largestNumber=number2
		else:
			largestNumber=largestNumber
		x=x+1	
	return largestNumber
print compareNumberToFirstOne()	







