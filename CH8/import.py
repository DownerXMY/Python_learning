import sys
print(sys.path)

if '/Users/xmy/PycharmProjects/Basic_Learning' not in sys.path:
    sys.path.append('/Users/xmy/PycharmProjects/Basic_Learning')

# from CH8.package_demo.math_package import my_sum

# 下面，我们来说说import语句的问题，我们已经知道了以下写法：
# import sys:import整个库
# from CH8.package_demo.math_package import my_max:从一个库中import一个'属性'(函数，变量，方法，...)

import sys
print(sys.version_info)

from sys import version_info
print(version_info)
# 那同理，比如之前在虚拟环境中的操作也可以类似地实现。
# 如果说要把一个库中的所有'属性'全部import，除了直接import库之外，也可以这么写：
from sys import *
# 但是这种方法是不建议的。

# 最后在一个复杂项目中，往往会调用很多库，那么import的顺序是怎么样的呢？
# 优先系统内置模块，其次是第三方模块，最后是自己写的模块。

# 学习了虚拟环境以后，我们就知道了安装第三方库有好几种不同的方法：
# 1.在pycharm的interpreter下点加号安装。
# 2.在终端中(先进入虚拟环境)，利用pip install的方法安装。
# 注意进入虚拟环境的方法是:假如虚拟环境的项目名字是demo，那么首先进入demo，然后source venv/bin/activate

from CH8.package_demo.math_package import my_sum
print(my_sum(1, 7, 4, 3))
# 这时候问题就来了，我们调用了my_sum，那么库中和my_sum有关的东西就全部被执行了。
# 这显然不是我们希望的结果， 那么该怎么控制呢？
# 那么这个时候就要用到if __name__ == '__main__'了。


