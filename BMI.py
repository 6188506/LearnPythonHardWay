#-*- coding: utf-8 -*-
weight = float(raw_input("�����������"))
height = float(raw_input("����������"))
BMI = weight / height * height

print('����BMIָ��Ϊ��')
if BMI < 18.5:
	print'���ع���'
elif 18.5 <= BMI <= 25:
	print'��������'
elif 25 <= BMI <= 28:
	print'���ع���'	
elif 28 <= BMI <= 32:
	print'����'
else:
	print'���ط�����'		