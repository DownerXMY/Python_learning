# from CH8.package_demo.math_package import my_sum
# print(my_sum(3,5,2,4))
# 注意我们模块检索路径尽量从最大的文件夹开始写起。

import sys
print(sys.path)

# 我们会发现在PyCharm和在本地中两个地址不一样，所以在本地运行python3.7 test.py会报错，说文件找不到
# 那么有什么解决办法呢，很简单我们可以把地址加进去。
if '/Users/xmy/PycharmProjects/Basic_Learning' not in sys.path:
    sys.path.append('/Users/xmy/PycharmProjects/Basic_Learning')
from CH8.package_demo.math_package import my_sum
print(my_sum(2,6,1,4))
# 那么这样以后，在终端也能够运行了，不会报错说找不到模块。
# 到此为止，有关于模块和包的基本内容就这么多了。
