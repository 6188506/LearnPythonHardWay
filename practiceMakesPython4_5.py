from collections import Counter
c = locals()
for index, word in enumerate(words):
	c['cou'+str(index)]=Counter()
	for letter in word:
		c['cou'+str(index)][letter] = c['cou'+str(index)][letter] + 1li