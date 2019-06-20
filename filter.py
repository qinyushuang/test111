def func(num):
    if num ** 2 > 100:
        return num

l = [1, 10, 8, 9, 12, 22]


print filter(func, l)