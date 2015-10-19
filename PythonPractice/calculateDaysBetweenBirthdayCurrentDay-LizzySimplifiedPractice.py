#用这个程序来练习def，return以及函数中的参数如何相互作用。这是我在学习coding以来的一个难点，花费时间最长。
#目前的心得： 程序的搭建从总到分。上一级的程序中用到的函数要在下一级定义。但是在上一级程序创建中就要考虑好下一级函数需要哪些参数。函数中的参数是此函数执行中需要的值。而函数的执行结果亦即return的值要满足上一级函数的需要。
#eg：若是判断，则需要返回True或者False，其他：需要哪些数值等等。

#这个code是简化Udacity的练习，把年月日的计算简单化成月日的计算，主要是为了test自己写的程序是否正确。是第一个自己写的函数嵌套的程序。
#没有涉及数值有效性的判断，也没有涉及闰年的计算。

#getTwoDates
#printResult(totalDatsBetweenTwoDates)

def calculateDaysBetweenTwoDates(birthMonth,birthDay,currentMonth,currentDay):
	if twoDaysWithSameMonth(birthMonth,currentMonth):
		return currentDay-birthDay
	else:
		return twoDaysWithDifferentMonth(birthMonth,birthDay,currentMonth,currentDay)

def twoDaysWithSameMonth(birthMonth,currentMonth):
	if birthMonth==currentMonth:
		return True
	else:
		False

def twoDaysWithDifferentMonth(birthMonth,birthDay,currentMonth,currentDay):
	days=0
	while birthDaybeforeCurrentDay(birthMonth,birthDay,currentMonth,currentDay):
		birthMonth,birthDay=nextDay(birthMonth,birthDay)
		days=days+1
	return days

def nextDay(birthMonth,birthDay):
	monthOf31days=[1,3,5,7,8,10,12]
	monthOf30days=[4,6,9,11]
	if birthMonth in monthOf31days:
		if birthDay<31:
			return birthMonth,birthDay+1
		else:
			return birthMonth+1, 1
	if birthMonth in monthOf30days:
		if birthDay<30:
			return birthMonth, birthDay+1
		else:
			return birthMonth+1, 1
	else:
		if birthDay<28:
			return birthMonth, birthDay+1
		else:
			return birthMonth+1, 1
		
	
def birthDaybeforeCurrentDay(birthMonth,birthDay,currentMonth,currentDay):
	if birthMonth<currentMonth:
		return True
	if birthDay<currentDay:
		return True
	else:
		return False	
print calculateDaysBetweenTwoDates(11,9,12,9)
print calculateDaysBetweenTwoDates(1,9,2,9)
print calculateDaysBetweenTwoDates(2,9,3,9)
print calculateDaysBetweenTwoDates(1,9,12,19)