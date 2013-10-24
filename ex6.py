# Defines x as a string including an integer equal to 10
x = "There are %d types of people." % 10
# defines the variable binary as the string binary
binary = "binary"
# defines the variable do_not as don't
do_not = "Don't"
# defines the variable y as a string that includes two other string variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints x
print x
# Prints y
print y

# Prints a string that includes x in single quotes
print "I said: %r." % x
# Prints a string that includes another string with a value of Y
print "I also said: '%s'." % y

# defines the variable hilarious as false
hilarious = False
# defines the variable joke_evaluation as a string that includes the hilarious variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints 2 variables
print joke_evaluation % hilarious

# Defines w as a string
w = "this is the left side of..."
# Defines e as a string
e = "a string with a right side."

# Prints the two strings side by side
print w + e