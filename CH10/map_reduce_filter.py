# Python的两个内置高阶函数：
# map传入一个函数和一个列表，函数作用在列表的每一个元素上，生成一个新的列表，传出。
print(map(lambda x: x * x + 1, [1, 2 ,3 ,4]))
# 会看到这样实际上是打印不出来的，不过可以这么做：
for i in map(lambda x: x * x + 1, [1, 2 ,3 ,4]):
    print(i, end = '--')
print('\n')
# 当然想要打印出来，也可以采用我们之前讲的列表解析的方法：
print([i for i in map(lambda x: x * x + 1, [1, 2 ,3 ,4])])

# 我们之前的问题，求斐波那契的第十个元素：
# 最基本方法：
s = 1
k = 1
m = 1
for i in range(1,9,1):
    m = k + s
    s = k
    k = m
print(m)

# 采用函数递归的方法：
def fbnq(n):
    if n == 1 or n == 2:
        return 1
    return fbnq(n-2) + fbnq(n-1)
print(fbnq(10))

# reduce高阶函数：
# reduce是需要引入内置模块的。
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

# 高阶函数filter，直观上翻译过来，就可以叫做过滤函数：
f = filter(lambda x: x % 2 == 0, [1, 2, 3 ,4 ,5 ,6])
print([i for i in f])



