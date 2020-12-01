import sys
print(sys.path)

if '/Users/xmy/PycharmProjects/Basic_Learning' not in sys.path:
    sys.path.append('/Users/xmy/PycharmProjects/Basic_Learning')
# 有一个自然地问题是，这个sys究竟是什么呢？为什么可以被直接import呢？
# 实际上sys是一个内置的模块，是安装时候就系统自己植入的。
# 但比如之前的package_demo就是我们自己写的模块。
# 除了系统内置的模块和我们自己写的模块外，还有一种叫做第三方模块，是别人写的，通常我们是要去安装调用的。
# 接下去，我们就来看看最重要的第三方模块。
# 新建一个project，名字是demo，接下去的操作会在demo中展示。
