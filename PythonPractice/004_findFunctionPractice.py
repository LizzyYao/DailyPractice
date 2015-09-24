# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1


# ENTER CODE BELOW HERE
def findZipPosition(text):
	firstPosition=text.find("zip")
	secondPosition=text.find("zip",firstPosition+1)
	print secondPosition

text = 'all zip files are zipped'
findZipPosition(text)
text ='all zip files are compressed'
findZipPosition(text)



