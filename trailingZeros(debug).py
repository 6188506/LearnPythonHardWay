def trailingZeros(x):
    n = 0
    result = reduce(lambda a,b : a*b, range(1, x+1))
    while result%10 == 0:
        result = result%10
        n += 1
    print n    