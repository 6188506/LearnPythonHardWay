def matrix(n):
	if n == 1:
	    print 'x'
	else:
	    result = []
	    for i in range(n):
                result.append('x')
            print '+'.join(result)
            n -= 1
            matrix(n)