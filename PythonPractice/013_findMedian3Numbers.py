#Anyway, GOOD JOB!!! LIZZY!!! :)
#This code took me such a long time to figure out. There might be a built in median function in python,
#but the request is only to use the knowledge obtained within this course so far. 
#thinking is interesting! I am wondering how the built-in "median" function code looks like,
# there must be some order/sort number function involved. then how "order/sort" function looks like.
# WOW, it's such a complicated question..........

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def median(a,b,c):
    if a >= b:
        if b>=c:
            return b
        else:
            if a>c:
                return c
            else:
                return a
    else:
         if a>=c:
            return a
         else:
            if b>=c:
                return c
            else:
                return b






print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7