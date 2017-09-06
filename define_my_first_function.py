def test(coke_count, fry_count, people_count):
	print "We total need %d cokes and %d fries" % (coke_count*people_count, fry_count*people_count)

print "We'll have a party on this sunday."
coke_count = int(raw_input("How many cokes do you need per person? "))
fry_count = int(raw_input("How much fries do you need per person? "))
people_count = int(raw_input("How many people do you have? "))
test(coke_count, fry_count, people_count)