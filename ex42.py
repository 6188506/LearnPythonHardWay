## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??
class Dog(animal):

	def __init__(self, name):
		##??
		self.name = name

## ??
class Cat(animal):

	def __init__(self, name):
		##??
		self.name = name

## ??
class Person(object):
	
	def __init__(self, name):
		##??
		self.name = name

    ## Person has-a pet of some kind
    self.pet = none

## ??
class Employee(person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??		
class Fish(object):
	pass
	
## ??	
class Salmon(Fish):
	pass

## ??
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank.pet = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

	
