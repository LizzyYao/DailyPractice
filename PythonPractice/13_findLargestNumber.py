#find largest number in 3 numbers.

def largestNumber():
	def getNumberFromUser(ordinal):
	#"get the numbers from user and convert string to float numbers."
		number=raw_input("please enter " + ordinal + " number: ")
		number=float(number)
		return number

	def findLargestNumber(number1,number2,number3):
	#evaluate each statement to find the largest number.

		if number1>=number2:
			if number2>=number3:
				return number1
			else:
				if number1>=number3:
					return number1
				return number3
		else:
			if number1>number3:
				return number2
			else:
				if number2>number3:
					return number2
				return number3
		
		

	number1=getNumberFromUser("first")
	number2=getNumberFromUser("second")
	number3=getNumberFromUser("third")
	print findLargestNumber(number1,number2,number3)
largestNumber()





