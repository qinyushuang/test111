# !/usr/bin/env python30
# _*_ coding:utf-8 _*_

# 迭代器
#  不能返回去访问，只能重新生成一个迭代器 使用iter()生成迭代器，next() 访问元素，超出边界会抛异常 StopIteration

l = [1, 2, 3, 4, 5]
it = iter(l)
print it
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next() # 这里会报错 StopIteration
