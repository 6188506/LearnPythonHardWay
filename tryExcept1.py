# -*- coding: UTF-8 -*-

a = int(raw_input("输入被除数: "))
b = int(raw_input("输入除数: "))
#c = a / b
try:
	print "算式为 %d ÷ %d = %d" % (a, b, a / b)

except ZeroDivisionError:
	print "除数不能为零"
	#print e.message

else:
	print "done"	# 没有发生异常，try部分执行，else部分才执行；	