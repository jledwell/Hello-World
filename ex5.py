name = 'Zed A. Shaw'
age = 35 # total lie 
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'no'

print "Let's talk about %r." % name
print "He's %d inches tall." % height

# convert inches to centimeters
print "That's about %d centimeters tall." % (round(height / 0.39370))
print "He's %d pounds heavy." % weight

# convert lbs to kilos
print "That's about %d kilos." % (round(weight / 2.2))

print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)