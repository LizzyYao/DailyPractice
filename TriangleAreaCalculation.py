import math
a=float(input("please enter the first side: "))
b=float(input("please enter the second side: "))
c=float(input("please enter the third side: "))
p=(a+b+c)/2
#use Heron's formula to get the area of the triangle,
#I can only understand this formula,
#It's time-consuming for me to figure out other formulas.
S=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
print "the area of this triangle you entered is: ",S

