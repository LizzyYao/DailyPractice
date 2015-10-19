def findPrimeNumberList(numberList):
	primeList=[1]
	x=min(numberList)
	y=max(numberList)
	while x<y:
		for i in numberList:
			if i%x==0:
				numberList.remove(i)
		primeList.append(x)
		x=min(numberList)
		y=max(numberList)
	return primeList
print findPrimeNumberList(range(2,301))
