#find largest number in 3 numbers.

def userInput(ordinal):
#get the numbers from user and convert string to float numbers.
	number=raw_input("please enter " + ordinal + " number: ")
	number=float(number)
	return number
	
number1=userInput("first")
number2=userInput("second")
number3=userInput("third")


def process():
#evaluate each statement to find the largest number.
	if number1>number2 and number1>number3:
		largestNumber=number1
	elif number2>number3 and number2>number1:
		largestNumber=number2
	else:
		largestNumber=number3
	return largestNumber
		
largestNumber = process()
	
def output(largestNumber):
	print("The largest number in {} {} and {} is: {}".format(number1,number2,number3,largestNumber))


output(largestNumber)



