# -*- coding: UTF-8 -*-
x = int(raw_input("������һ�����֣� "))

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	elif x >= 0:
		print x
	else:
		print -x		
		
my_abs(x)		
		