def find_uniq(arr):
    arr_tran = [set(i.replace(' ','').lower()) for i in arr]
    arr_tran1 = [arr_tran[0]==i for i in arr_tran]
    if arr_tran1.count(False)==1:
        return arr[arr_tran1.index(False)]
    else:
        return arr[0]
