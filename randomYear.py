import random

year = random.randint(0, 99)
print "You are %d years old." % year

if year<=3:
	print "You are a toddler!"
elif 3<year<=5:
	print "You are a preschooler!"
elif 5<year<=12:
	print "You are a schoolchild!"	
elif 12<year<=19:
	print "You are a teenager!"	
elif 19<year<=40:
	print "You are a young person!"	
elif 40<year<=65:
	print "You are a middle age person!"		
else:
	print "You are an old person"
