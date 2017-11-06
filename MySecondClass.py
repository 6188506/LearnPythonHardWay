class Income(object):
	def __init__(self, name, age, gender, salary):
		self.name = name
		self.age = age
		self.gender = gender
		self.salary = salary

	def print_information(self):
		print "You name:%s;age:%d;gender:%s;salary:%d" % (self.name, self.age, self.gender, self.salary)


	def sal_level(self):
		if self.salary >= 1000000:
			print "You are TuHao!" 	
		elif 500000 <= self.salary <100000:
			print "You are middle class!" 
		else:
			print "You are poor"	
