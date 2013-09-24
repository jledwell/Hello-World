print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Counting 1 to 10!"
while True:
	for i in ["1","2","3","4","5","6","7","8","9","10"]:
		print "%s\r" % i
		raw_input("Press Enter to continue, or CTRL-C to end ...")