# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

# let's try use recursion to fullfil this 

def factorial(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
