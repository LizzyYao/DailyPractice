# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    greatestNumber=0
    for i in list_of_numbers:
        if i>greatestNumber:
            greatestNumber=i
        else:
            greatestNumber
    return greatestNumber



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0