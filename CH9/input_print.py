print('hello', 'world', sep = '--')

import sys
sys.stdout.write('hello--world')
# 可以看到这两个结果是一样的，换句话说，print默认的就是标准输出。

a = input('标准输入')
print(a,type(a))
# 换句话说，标准输入只会接收字符串。

a = sys.stdin.readlines()
print(a,type(a))
# 惊奇地发现，这时候输入的数据类型变成了list，而且是根据回车做的一个list



