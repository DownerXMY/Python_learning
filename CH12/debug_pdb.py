# pdb方法是比较专业强大的debug方法
# 比如还是上次的例子：

import pdb
pdb.set_trace()

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
# 那么怎么用pdb呢？
# 需要调用内置模块pdb
# 注意这时候再运行，没有报错，但是出现了Pdb的提示符。
# 这时候我们在终端运行:python3.7 + pdb的地址，就能够在终端进入pdb的模式
# ?--查看有哪些命令，s--一行行执行，n--直接运行，l--查看临近的代码
# 当然记得用pdb调试完成后，要把开头两行删掉，否则程序就没法正常运行了。

