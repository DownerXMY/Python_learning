# 介绍内置模块collections
from collections import *
# This module implements specialized container datatypes providing

# tuple的深入理解：
a = (1, 2, 3, 4)
# 之前我们已经说过很多tuple的性质和操作，比如说遍历，检索，访问等等
# 当然还有一些没介绍的，比如：
n = 0
print('''"sequence unpacking:"''') # 按顺序分别赋值
for item in ('x', 'y', 'z', 'w'):
    n = n + 1
    t = item
    x, y, z, w = a
    print(f'{t} =', a[n-1])
# 在以上例子中，比如我们不关心元组a的第二个位置的元素，就可以用下划线忽略掉:
x1, _, x3, x4 = a
print(x1, x3, x4)
# 只关心元组的第一个元素:
y1, *_ = a
print(y1)
# 想把第二个元素以后的元素全部赋给一个列表：
z1, *all_elements_left = a
print(z1, all_elements_left)

# --------------------------------------------------------------
# 什么是named tuple？
# 比如我们现在有一个很简单的类：
class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.__school = school
    @property
    def school(self):
        return self.__school
    @school.setter
    def school(self, school):
        self.__school = school
    def Sayhello(self):
        print(f'Hello, I am {self.name}, I am {self.age} years old, I am from {self.school}')
Mingyue_Xu = Student(name = 'Mingyue_Xu', age = 22, school = 'SJTU')
Haoyu_Shi = Student(name = 'Haoyu_Shi', age = 22, school = 'ZJU')
Mingyue_Xu.Sayhello()
Haoyu_Shi.Sayhello()
# 为什么要引入named tuple呢？
# 那比如我们就定义这么两个元组：
Mingyue_Xu = ('Mingyue_Xu', 22, 'SJTU')
Haoyu_Shi = ('Haoyu_Shi', 22, 'ZJU')

# 这里有一件事情不容易引起注意，就是我们也可以通过元组访问元素的方式访问到元素，虽然看似更加简单，但是：
# 如果没有class，或许我们不会知道Mingyue_Xu表示的是一个人的名字，22表示的是一个人的年龄。
# 我们看到了，使用class去访问元素，和直接访问元组的两种方式各有各的优势劣势
# named tuple就是为了综合这两种方式的优劣：

from collections import namedtuple
Variable = namedtuple('Tuple_Name', ['name', 'age', 'school'])
# 怎么理解？
# namedtuple实际上是一个函数，所以它需要接收参数，只不过我们这里传入的参数是'属性'。
# 'Tuple_Name'就是名字，后面的向量就是字段。
# 这样一来，我们就可以去实例化了，可以想象成一个需要传入参数的变量：
S1 = Variable('Mingyue_Xu', 22, 'SJTU')
S2 = Variable('Haoyu_Shi', 22, 'ZJU')
a = []
a.append(S1)
# 换句话说，用比class简单的方式完成了class能做到的工作
print(a[0].name)
print(S2.age)
print(S2.school)
# 可以说namedtuple是一个比较高级的数据类型。

# ----------------------------------------------------------------
# 什么是default_dict?
word_list = ['love', 'hello', 'conflate', 'love', 'hello', 'definition', 'love', 'randomly', 'conflate']
# 我们想通过建立一个字典的方式去统计一下每个单词出现的次数
# 当然我们可以直接做：
result = dict()
for item in word_list:
    if item not in result:
        result[item] = 1
    else:
        result[item] = result[item] + 1
print(result)

result1 = dict()
for item in word_list:
    result1.setdefault(item, 0) # 设置默认值为0，简化判断逻辑
    if item in result1:
        result1[item] = result1[item] + 1
print(result1)

# 现在我们来看看default_dict:
from collections import defaultdict
result2 = defaultdict(list)
# 我们先来看看default_dict是什么东西？
print(result2, type(result2))
# 是一个defaultdict对象，是一种高级的数据类型。
# 那么神奇的事情在哪里呢？我们知道如果对于一个字典，我们想要去访问一个key不存在的元素，会报错KeyError:
# a = {}
# print(a['a'])
# 但是对于defaultdict就是不会有这种问题：
print(result2['a'])
# 并且更加重要的是，他还兼具了初始化的功能，比如：
print(result2['b'])
print(result2['c'])
print(result2)
# 这时候'a','b','c'这三个key值已经存在了，且对应的value都是[]，因为我们当时设定的类型就是list.
# 现在我们就是要利用这种特性完成统计单词出现次数的工作：
word_list = ['love', 'hello', 'conflate', 'love', 'hello', 'definition', 'love', 'randomly', 'conflate']
result3 = defaultdict(int)
for item in word_list:
    result3[item] += 1
print(result3)
# 这时候就不需要任何判断了。
# 更深入一点，我们还可以做一个比较复杂的初始化：
def set_defaultdict():
    return {'name': '', 'age': 0}
result4 = defaultdict(set_defaultdict)
# 实际上是一个字典中的字典。
print(result4['Mingyue_Xu'])
print(result4)
# 这样我们相当于是运用defaultdict完成了一个在class中做的工作。

# -------------------------------------------------------------------
# 什么叫deque?
# deque是一个双向队列，换句话说，能对头和尾都进行插入，删减，等等操作
# 大概感觉deque还是非常实用的。
from collections import deque
d = deque([1, 2, 3, 4, 5, 6])
d.append(7)
print(d)
d.appendleft(0)
print(d)

d.extend([8, 9, 10])
print(d)
d.extendleft([-1, -2, -3])
print(d)
# 等等类似在列表里的操作都可以双向实现。
# deque在什么情况下会非常有用呢?
# 比如如果说元素个数比较大：
import time
d1  =list(range(100000000))
d2 = deque(range(100000000))
t1 = time.time()
d1.insert(5000000, 'abc')
print('list:', time.time() - t1)
t2 = time.time()
d2.insert(5000000, 'abc')
print('deque:', time.time() - t2)
# 惊奇地发现类似于'检索某个位置'的操作，采用deque，运算效率会高出一大截。这是非常重要的，尤其是在大项目中。
# list: 2.7580230236053467
# deque: 0.17456626892089844
# 但是比如说如果操作是append，那么还是list会稍微快一点点，不过差别不大，时间都很短。

# ---------------------------------------------------------------------
# 什么是counter？
from collections import Counter
word_list = ['love', 'hello', 'conflate', 'love', 'hello', 'definition', 'love', 'randomly', 'conflate']
# 统计每个单词出现的次数，我们之前已经用defaultdict非常高效地完成了。
result_1 = defaultdict(int)
for word in word_list:
    result_1[word] = result_1[word] + 1
print(result_1)
# 那么实际上用counter是可以更快完成的:
c = Counter(word_list)
print(c)
# 这样就好了，Counter的传入对象也可以是字符串：
s = 'jdfkanvkavnanfkna'
print(Counter(s))
# 不仅如此，Counter还可以统计出比如:出现次数最多的字母是哪个，这类的问题：
c2 = Counter(s)
print(c2.most_common(3)) # 打印出出现次数TOP3的字母
# 当然还有很多操作，比如说求和，排序等等
c2.update('jfbjcrajbkebfjkb') # 新增元素以后重新统计
print(c2.most_common(3))

# ----------------------------------------------------------------------
# 什么是ordered_dict?
# 假如我们初始化一个字典:
d3 = dict()
d3['a'] = 1
d3['b'] = 2
d3['c'] = 3
print(d3)
# 可以看到它是按照我们初始化的顺序来写入字典的，比如先写入'a',然后是'b'

from collections import OrderedDict
d4 = OrderedDict()
d4['a'] = 1
d4['b'] = 2
d4['c'] = 3
print(d4)
d4.move_to_end('a')
print(d4)
# 通过打印，我们发现了一个和普通字典相比非常重要的区别：
# 就是OrderedDict是一种高级的数据类型，其中的元素是以tuple的形式存在的。


