#-*- coding=utf-8 -*-
#必须在python 3.x环境下

import urllib.request
import re
number = 12345

for i in range(400):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'%number
	
	if i == 85:
		url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=two'
	f = urllib.request.urlopen(url)
	webPage = f.read().decode()                  #=>网页的内容并从bytes转换成string
	number = int(re.findall('\d{3,8}', webPage)[0])
	
	print(webPage)
	print(i)
    
print (number)



i = 355  得到了结果peak