#! /user/bin/env python
def is_prime(n):
	from math import sqrt 
	if n == 1:
		return False
	for i in range(2, int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	return True		