# Pycharm自身也是有debug的能力的：
# 比如还是老例子：
a = [1, 4, 3, 11, 8, 6, 12, 5, 7]
def all_odd(t):
    s = []
    for i in range(1,len(t)+1,1):
        if t[i-1] % 2 == 0:
            continue
        else:
            print(t[i-1])
            s.extend(t[i-1])
    return s
print(f'列表{a}中的所有奇数项为{all_odd(a)}')
# 利用pycharm去debug，首先要设置一个断点。
# 比如，我觉得在第6行以前的代码都是没问题的，想让代码从第6行开始一行行地执行，那么就在第6行设置一个断点。
# 然后有三个不同的按钮，可以灵活选择查看方式。


