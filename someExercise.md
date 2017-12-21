对于列表形如list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]转化成列表list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]的问题。
+    函数： 
```def split_list(x):
       list_2 = []
       for e in range(len(x)): 
           for y in range(len(x[e])):
		       list_2.append(x[e][y])
        return list_2 ```


普通方法： 
list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
list_2 = []
for _ in list_1:
    list_2 += _
print(list_2)

列表推导：list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
[i for k in list_1 for i in k]


