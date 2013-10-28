from sys import argv

script, user_name, penis_size = argv
prompt = '> '

print "Hi %s with the %s inch penis, I'm the %s script." % (user_name, penis_size, script)
print "I'd like to ask you a few questions."
print "Do you like me %s? with the %s inch penis" % (user_name, penis_size)
likes = raw_input(prompt)

print "Where do you live %s with the %s inch penis?" % (user_name, penis_size)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)