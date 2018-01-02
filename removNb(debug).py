def removNb(n):
    result = []
    for a in range(1, n+1):
	    for b in range(1, n+1):
		    if sum(range(1, n+1))-(a+b)==a*b:
			    result.append((a,b))
    return result