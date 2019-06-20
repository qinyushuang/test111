# coding:utf-8

# 生成器
# 如果列表元素可以根据某个算法生成出来，这样就不用创建list，可以边循环边计算出来，这样可以节省大量的存储空间
# 这种一遍循环一遍计算的机制就是生成器 ，例如: yeild 就是创建了一个生成器
# 生成器用()， 不是[] 也不是{}

g = (x * x for x in range(10))
print g

print g.next()
print g.next()
print g.next()
print g.next()


for item in g: # 前面几条语句已经访问了前4个元素，这时候生成器从第五个元素开始继续访问
    print item