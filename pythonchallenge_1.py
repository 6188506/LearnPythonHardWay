def convert_alp(text):
	result = []
	for i in text:
		print i
		if 97<=ord(i)<=120:
		    result.append(chr(ord(i)+2))
		elif ord(i) == 121:
			result.append(chr(97))
		elif ord(i)	== 122:
			result.append(chr(98))
		else:	
			result.append(i)
	print ''.join(result)	
	
#using string.maketrans() is recommended.(我要查下怎么使用！)	