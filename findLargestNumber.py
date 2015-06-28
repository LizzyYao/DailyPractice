#find largest number in 3 numbers.

number1=input("Please enter 1st number: ")
number2=input("Please enter 2nd number: ")
number3=input("Please enter 3rd number: ")
#convert string to float number.
number1=float(number1)
number2=float(number2)
number3=float(number3)


#find largest number
def getNumbers(number1,number2,number3):
    print number1,number2,number3
    return number1,number2,number3
getNumbers(number1,number2,number3)

if number1>number2 and number1>number3:
	largestNumber=number1
elif number2>number3 and number2>number1:
	largestNumber=number2
else:
	largestNumber=number3

def findLargestNumber(largestNumber):
	print largestNumber
	return largestNumber
findLargestNumber(largestNumber)

#output largest number
def printLargestNumber():
    print "The numbers you entered are {} {} and{}, ".format(number1,number2,number3)
    print "The largest number among these numbers is: {}".format(largestNumber)

printLargestNumber()

