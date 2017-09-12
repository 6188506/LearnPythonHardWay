#-*- coding: utf-8 -*-
weight = float(raw_input("输入你的体重"))
height = float(raw_input("输入你的身高"))
BMI = weight / height * height

print('您的BMI指数为：')
if BMI < 18.5:
	print'体重过轻'
elif 18.5 <= BMI <= 25:
	print'体重正常'
elif 25 <= BMI <= 28:
	print'体重过胖'	
elif 28 <= BMI <= 32:
	print'肥胖'
else:
	print'严重肥胖了'		