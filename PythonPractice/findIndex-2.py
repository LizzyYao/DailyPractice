# different way of finding element in a list and return index of the element. use for loop with index attritute.

# If there is no matching element,
# return -1.

def find_element(list, value):
    for m in list:
        if m==value:
            return list.index(m)
    return -1




print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1