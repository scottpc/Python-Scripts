from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()

print "Okay, so you are currently running", script
print "You are also using variable", first, second, third
print "and you are %r years old." % age
print "as well as %r tall." % height