my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74.0 # inches
my_weight = 180.0 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
height_feet = my_height / 12.0
weight_kg = my_weight * 0.453592

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "You could also say that I'm %d feet tall." % height_feet
print "You could also say that I'm %d kg heavy." % weight_kg
	
# %d prints an integer
# %s prints a string