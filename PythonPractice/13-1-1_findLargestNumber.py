
#find largest number in 5 numbers.

#"get the numbers from user and convert string to float numbers."
def getNumbersFromUser():		
	x=1
	numberList=[]
	while x<=5:
		number=float(raw_input("please enter your number: "))
		numberList.append(number)
		x=x+1
		
	return numberList	

numberList=getNumbersFromUser()
def findLargestNumber():
	return max(numberList)

largestNumber=findLargestNumber()
def outPutLargestNumber():
	
	print "The largest number is: ", largestNumber


outPutLargestNumber()

#after figured out how to use list.append attribute properly and modified this code.





