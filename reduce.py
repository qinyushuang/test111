# _*_ coding:utf-8 _*_
# from functools import reduce

l = [1, 2, 3, 4, 5]
print reduce(lambda x, y: x + y, l)

print reduce(lambda x, y: x + y, l, 5) # 这里5可以认为是初始值