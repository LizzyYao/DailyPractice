#find largest number in 3 numbers.

<<<<<<< HEAD
#get the numbers from user and convert string to float numbers.

def NumberFromUser(ordinal):
=======
def userInput(ordinal):
	"get the numbers from user and convert string to float numbers."
>>>>>>> ab5afbef6c9fdfb015abb99478b9d11d754d8670
	number=raw_input("please enter " + ordinal + " number: ")
	number=float(number)
	return number
	
number1=NumberFromUser("first")
number2=NumberFromUser("second")
number3=NumberFromUser("third")

<<<<<<< HEAD
def FindLargestNumber():
#evaluate each statement to find the largest number.
=======

def process():
	"evaluate each statement to find the largest number."
>>>>>>> ab5afbef6c9fdfb015abb99478b9d11d754d8670
	if number1>number2 and number1>number3:
		largestNumber=number1
	elif number2>number3 and number2>number1:
		largestNumber=number2
	else:
		largestNumber=number3
	return largestNumber
		
largestNumber = FindLargestNumber()
	
def PrintLargestNumber(largestNumber):
	print("The largest number in {} {} and {} is: {}".format(number1,number2,number3,largestNumber))


PrintLargestNumber(largestNumber)




