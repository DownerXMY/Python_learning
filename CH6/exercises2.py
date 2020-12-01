# 写函数，利用递归获取斐波那契数列中的第10个数，并将该值返回给调用者。
def fbnq(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fbnq(n-1) + fbnq(n-2)
print(fbnq(n = 10))

# 编写程序，输入一个包含若干自然数的列表，输出一个新列表，每个元素为原列表中每个自然数的位数。
def account(a):
    b = []
    for i in range(1,len(a)+1,1):
        b.append('0')
    # print(b)
    for j in range(1,len(a)+1,1):
        s = f'{a[j-1]}'
        b[j-1] = len(s)
    return b
a1 = eval(input('请输入一个列表'))
print(account(a = a1))

# 输入一个包含若干整数的列表，输出这些整数的乘积。
# 不用递归
def multiple(c):
    result = 1
    for i in range(1,len(c)+1,1):
        result = result * c[i-1]
    return result
c1 = eval(input('请输入一个列表'))
print(multiple(c = c1))
# 使用递归
def multiple1(d, n):
    if n == 0:
        return 1
    return d[n-1] * multiple1(d, n-1)
d1 = eval(input('请输入一个列表'))
n1 = int(input('请输入一个数字'))
m = len(d1)
while n1 > m:
    print('The request is invalid!')
    n1 = int(input('请重新选择一个数字!'))
print(multiple1(d = d1, n = n1))
# 并不是递归一定更加方便的，比如在此例中采用递归的话，则需要判断的条件就会变多。

# 编写一个函数，输入一个数字n，如果是偶数，则输出n/2，如果是奇数，则输出(3n+1)/2. 这道题请采用函数调用函数的方式。
def judge1(n):
    return n / 2
def judge2(n):
    return (3 * n + 1) / 2
def judge(t, **k):
    if t:
        return judge1(**k)
    else:
        return judge2(**k)
n1 = int(input('请输入一个正整数'))
m = 0
while n1 > 0:
    m = m + 1
    if (n1 % 2) == 0:
        t1 = True
    else:
        t1 = False
    print(judge(t = t1, n = n1))
    if m >= 3:
        break
    n1 = int(input('您还可以继续尝试!'))
##############################################
