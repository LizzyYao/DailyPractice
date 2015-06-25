import math
miles=float(input("Please enter the number of miles: "))
convertFactor=1.60934
kilometres=miles*convertFactor
kilometres=round(kilometres,4)
print("the number of miles you entered: {} is equal to {} kilometres".format(miles,kilometres))
