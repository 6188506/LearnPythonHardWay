#=>Number guessing game
import random

the_guessed_number = random.randint(0,100)

user_guessing_number = int(input("我这里有0-100个数字请猜一下: "))
while True:
	if user_guessing_number == the_guessed_number:
		print("正确！")
		break
	elif user_guessing_number > the_guessed_number:	
		print("大了！")
		user_guessing_number = int(input("请重新输入: "))
		continue
	else:
		print("小了！")
		user_guessing_number = int(input("请重新输入: "))
		continue


