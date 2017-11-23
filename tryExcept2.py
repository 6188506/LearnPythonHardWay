try:
	a = 25 / 5
	print a
	print m
	b = 1 / 0
	print b 
	c = 2 / 1
	print c
except NameError,e:
	print 'Ops!',e	
except ZeroDivisionError,e:
	print e
except:
	print 'other Error'
else:
	print 'No Error!Yeah!!!'
finally:
	print "whatever,this is the END!"	