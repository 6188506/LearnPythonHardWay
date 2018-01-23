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
	
i hope you didnt translate it by hand. thats what computers are for. 
doing it in by hand is inefficient and that's why this text is so long.
 using string.maketrans() is recommended. now apply on the url	
#using string.maketrans() is recommended.(我要查下怎么使用！)	

必须在python3.x下完成

def convert_alp(text):
	instr = "abcdefghijklmnopqrstuvwxyz"
	outstr= "cdefghijklmnopqrstuvwxyzab"
	return text.translate(text.maketrans(instr, outstr))