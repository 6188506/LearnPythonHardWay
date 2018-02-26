def move_zeros(array):
    arr = filter(lambda x:type(x)==int,array)
    arr = filter(lambda x:x!=0,arr)
    for i in range(len(arry)-len(arr)):
        arr.append(0)
        
    return arr    
    