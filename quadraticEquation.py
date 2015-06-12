import cmath
#take three values from user. value a can not be 0
a=float(input("Please enter value (a): "))
if a==0:
	a=float(input("Please re-enter a non-zero value (a): "))
b=float(input("Please enter value (b): "))
c=float(input("Please enter value (c): "))

#get the squareroot of b^2-4ac, assign to variable d.
d=cmath.sqrt((b**2)-(4*a*c))

solution1=(-b+d)/(2*a)
solution2=(-b-d)/(2*a)

#I didn't spend too much time figuring out how to get the solution mathematically, only focus on how I can get my code work properly. 
print "You get 2 solutions: ",solution1, "and", solution2


