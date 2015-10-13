
#find largest number in 5 numbers.

#"get the numbers from user and convert string to float numbers."
def getNumbersFromUser():		
	x=1
	y=0
	numberList=[0,0,0,0,0]
	while x<=5:
		number=float(raw_input("please enter your number: "))
		numberList[y]=number
		x=x+1
		y=y+1
	return numberList	


def findLargestNumber():
	
	return max(getNumbersFromUser())

def outPutLargestNumber():
	
	print findLargestNumber()


outPutLargestNumber()

#Is this formating the one you requested(input process output)? my code is working, 
#but it looks so stupid that I have to put as many 0s there
# as the quantity of the mumber we would like to work with.




