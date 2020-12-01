# 程序很难保证没有错误，所以要学会如何发现错误和修正。
# 通过print语句进行调试：
a = [1, 4, 3, 11, 8, 6, 12, 5, 7]
def all_odd(t):
    s = []
    for i in range(1,len(t)+1,1):
        if t[i-1] % 2 == 0:
            continue
        else:
            s.append(t[i-1])
    return s
print(f'列表{a}中的所有奇数项为{all_odd(a)}')
# 以上代码当然是对的，不过如果做一点小小的改动，比如：
a = [1, 4, 3, 11, 8, 6, 12, 5, 7]
def all_odd(t):
    s = []
    for i in range(1,len(t)+1,1):
        if t[i-1] % 2 == 0:
            continue
        else:
            print(t[i-1])
            # s.extend(t[i-1])
            s.extend([t[i-1]])
    return s
print(f'列表{a}中的所有奇数项为{all_odd(a)}')
# 就会出现一个TypeError.
# 所谓print的方法就是，在之前打印看看t[i-1]是什么


