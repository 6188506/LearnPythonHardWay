def add(x):
    return x+x
arr = [add]
map(lambda x:x(5), arr)