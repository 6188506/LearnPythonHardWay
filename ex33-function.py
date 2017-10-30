#i = 0
numbers = []

def count_and_print_number(i):
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

for i in range(6):
	count_and_print_number(i)
	

print "The numbers: "

for num in numbers:
	print num 