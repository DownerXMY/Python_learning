def add2(a, b):
    return a + b
print(add2(1, 2))

def add3(a, b, c):
    return a + b + c
print(add3(1, 2, 3))

# 比如说我们要求很多数的和，总不至于要一直这样定义下去。
# 当然有一种办法是将参数定义成一个列表，比如：
def add(a):
    m = 0
    for i in range(1,len(a)+1,1):
        m = m + a[i-1]
    print(m)
add(a = [1, 6, 5, 2, 7 ,4, 3])

# 但是下面我们介绍可变参数的方法
def f_1(*args):
    print(args)
f_1(1, 2, 3, 4, 5)
# 注意这时候打印出来的args将会是一个tuple
# 那么，我们可以这样求和：

def add_1(*args):
    m = 0
    for i in range(1,len(args)+1,1):
        m = m + args[i-1]
    return m
s = add_1(1, 4, 7, 3, 6, 5, 2)
print(s)

# 当然不一定传入的参数必须是整数，只要不报错，在上例中就是能相加，即可。比如：
def add_2(*a):
    n = [0, 0, 0]
    for i in range(1,len(a)+1,1):
        n = n + a[i-1]
    return n
s_1 = add_2([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(s_1)

# 还有更加复杂但也更加实用的情况是，我们希望输入的参数既有关键字，也有可变参数，比如
# f(a = 1, 10, 11, 12)，那么在函数体中我们就能使用a了

def add_3(**kwargs):
    print(kwargs)
add_3(a = 1, b = 2)
# 可以看到打印出来的将是字典
# 那么受到启发，比如我们想计算a + b * c，就可以这么做：
def f_2(**k):
    m = k.get('a') + k.get('b') * k.get('c')
    return m

a1 = int(input('请输入a'))
b1 = int(input('请输入b'))
c1 = int(input('请输入c'))
s1 = f_2(a = a1, b = b1, c = c1)
print(s1)
# 这里有几点需要注意：
# 1. k.get('a')而不是k.get(a)
# 2. input前如果不加int，那么a1,b1,c1将都是str

# 当然**kwargs最常用的方式在于函数中调用另外的函数
def ADD(a, b):
    return a + b

def MUL(x, **k):
    if x == 10:
        return ADD(**k)

print(MUL(x = 10, a = 3, b = 8))

# 换句话说，当函数MUL要调用函数ADD时，并不关心ADD中的参数到底是什么有多少
# 另一个角度来看，有时候做调整的时候，完全可以原封不动MUL
# **k必须放在最后一位。
