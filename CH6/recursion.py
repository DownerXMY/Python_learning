# 一个简单的例子就是实现阶乘
def om(a):
    s = a
    while a >= 2:
        a = a - 1
        s = s * a
    return s
a1 = int(input('请输入一个整数'))
print(om(a = a1))

# 当然可以按照上面的写法，不过更好的是'递归'：
# n！相当于 n * (n-1)!
def om1(n):
    if n == 1:
        return n
    return n * om1(n-1)
print(om1(n = 5))
# 递归必须有一个跳出点，比如上面的n == 1，否则将报错。

