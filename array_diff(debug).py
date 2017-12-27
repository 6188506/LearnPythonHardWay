def array_diff(a, b):
    if len(a) == 0:
        return a
    elif len(a)==0 and len(b)==0:
        return a
    else:    
        for i in range(len(b)):
            if a.count(b[i]) > 1:
                while b[i] in a: 
                    a.remove(b[i])
            else:
                a.remove(b[i])
        return a
    #=>测试全过，但是提交时候出错