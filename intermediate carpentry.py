# !/usr/bin/env python
# -*- coding:utf-8 -*-

y = [ ('IBM', 5), ('Zil', 3), ('DEC', 18) ]
def sort_on_second(a, b):
    return cmp(a[1], b[1])

y.sort(sort_on_second)

print (y)