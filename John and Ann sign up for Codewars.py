def john(n):
    result = []
    counter = 0
    t = john(n-1)
    if counter <= n:
        if n == 0:
            result.append(0)
            counter += 1
        else:
            result.append(n - ann(t))
            counter += 1 
    return result    
    
def ann(n):
    result = []
    counter = 0
    t = ann(n-1)
    if counter <= n:
        if n == 0:
            result.append(1)
            counter += 1
        else:
            result.append(n - john(t))
            counter += 1 
    return result    
    
def sum_john(n):
    return sum(john(n)) 
    
def sum_ann(n):
    return sum(ann(n)) 