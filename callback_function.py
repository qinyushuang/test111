#!/usr/bin/python
# _*_ coding: utf-8 _*_

# 回调函数B作为另外一个函数A的参数，在另外一个函数A中被调用，
# 这种情况A函数相当于是提供私人定制的服务，回调函数相当于客户的个性化定制
# 例如一个旅店提供叫醒服务（相当于函数A）， 至于怎么叫醒是电话叫醒还是人工叫醒由客户决定（函数B）

# 回调函数1
def double(x):
    return x * 2
# 回调函数2
def triple(x):
    return x * 3

# 中间库函数， 用回调函数作为参数，并在中间函数中进行调用回调函数
def middle_func(k, func):
    return func(k) + 1

# 主程序中根据不通过的回调函数返回不同的中间函数结果
if __name__ == '__main__':

    print middle_func(1, double)
    print middle_func(1, triple)