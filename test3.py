#/usr/bin/python
# -*- coding:utf8 -*-

# python中class的__dict__包含了类的属性
class A():
    def __init__(self):
        self.x = 1  # 定义一个实例属性

    y = 2  # 定义一个类属性


a = A()
print a.__dict__
print a.y
print a.x
a.__dict__ = {}  # 清空实例的所有属性,y不受影响，因为他是类属性而非实例属性
print a.__dict__
print a.y
# print a.x  # 这里会提示不包含x属性的错误，因为已被清空
print A.__dict__
A.__dict__ = {}  # 清空类的所有属性，x不受影响
# print a.x
# print a.y  # 提示错误