def zeros(n):
    power = 1
    counter = 0
    for i in range(1,n+1):
        power = power * i
    power = map(int, list(str(power)))
    for index,value in enumerate(power[::-1]):
        if value == 0:
            counter += 1
        else:
            break
    return counter