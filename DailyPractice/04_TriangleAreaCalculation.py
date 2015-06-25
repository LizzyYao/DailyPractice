import math
triangleSideA=float(input("please enter the length of first side(cm): "))
triangleSideB=float(input("please enter the length of second side(cm): "))
triangleSideC=float(input("please enter the length of third side(cm): "))
parameter=(triangleSideA+triangleSideB+triangleSideC)/2
#use Heron's formula to get the area of the triangle,
#I can only understand this formula,
#It's time-consuming for me to figure out other formulas.
area=round(math.sqrt(parameter*(parameter-triangleSideA)*(parameter-triangleSideB)*(parameter-triangleSideC)),2)
print "the area of this triangle you entered is: ",area

