#!/usr/bin/python
# coding:utf-8

# 这里说明一个方法被多个装饰器装饰的时候，调用这个方法时函数的执行顺序
# @A
# @B
# @C
# def func(): xxx
# func 被A， B， C三个装饰器装饰:
#  - 在定义阶段，执行的顺序是C(B(A(func)))
#  - 在执行阶段，执行的顺序是A(B(C(func)))

def war1(func):
    print 'war1'
    def inner(*args, **kwargs):
        print "war1 start ========"
        func(*args, **kwargs)
        print "war1 end =========="
    return inner

def war2(func):
    print 'war2'
    def inner(*args, **kwargs):
        print "war2 start ========"
        func(*args, **kwargs)
        print "war2 end =========="
    return inner


@war1
@war2
def f():
    print '===== start ======'

f()

# 结果：
#war2               # 定义阶段的输出
#war1               # 定义阶段的输出
#war1 start ========  # 从这里开始是执行阶段的输出
#war2 start ========
#===== start ======
#war2 end ==========
#war1 end ==========