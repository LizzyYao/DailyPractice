def is_friend(name):
    return name[0]=="D" or name[0]=="N"



print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

print is_friend('')
