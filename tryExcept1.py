# -*- coding: UTF-8 -*-

a = int(raw_input("���뱻����: "))
b = int(raw_input("�������: "))
#c = a / b
try:
	print "��ʽΪ %d �� %d = %d" % (a, b, a / b)

except ZeroDivisionError:
	print "��������Ϊ��"
	#print e.message

else:
	print "done"	# û�з����쳣��try����ִ�У�else���ֲ�ִ�У�	