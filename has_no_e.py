i = t = 0
file = open('words.txt')
def has_no_letter(file, letter):
	for line in file:
		word = line.strip()
		i = i + 1
		if 'letter' in word:
			print word
			t = t + 1
	print "words have \'letter\' are %d%%" % (t * 100/ i)		
	