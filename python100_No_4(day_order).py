def day_order():
	sum_day = 0
	year = int(input("请输入年份"))
	month = int(input("请输入月份"))
	day = int(input("请输入日期"))
	big_month = [1, 3, 5, 7, 8, 10, 12]
	small_month = [4, 6, 9, 11]
		
	for i in range(1,month):
		if  i in big_month:
			sum_day += 31
		if  i in small_month:
			sum_day += 30
		if i == 2 and year%4 == 0:
			sum_day += 29
		if i == 2 and year%4 != 0:
			sum_day += 28
	return sum_day + day 		
			
		