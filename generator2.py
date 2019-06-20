# !/usr/bin/python
# coding:utf-8

'''
使用yield来返回生成器
'''

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

f = odd()
print f.next()
print f.next()
for item in f:
    print item