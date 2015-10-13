#find largest number in 4 numbers.


def getNumberFromUser(ordinal):
#"get the numbers from user and convert string to float numbers."
	number=raw_input("please enter " + ordinal + " number: ")
	number=float(number)
	return number

def findLargestNumber(number1,number2,number3, number4):
#evaluate each statement to find the largest number.

	return max(number1,number2,number3, number4)
	
	

number1=getNumberFromUser("first")
number2=getNumberFromUser("second")
number3=getNumberFromUser("third")
number4=getNumberFromUser("forth")
print findLargestNumber(number1,number2,number3, number4)





