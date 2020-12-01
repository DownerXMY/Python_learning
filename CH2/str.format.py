name = 'python'
age = 22

# 如何打印"我是python，今年22岁了"

# new_str = '我是' + name + ',' + '今年' + age + '岁了'
# print(new_str)
# 会显示运行错误
# 怎么把 int 类型的数据变成字符串呢？

new_str = '我是' + name + '，' + '今年' + str(age) + '岁了'
print('new_str = ' + new_str)

# 字符串的格式化方法1
new_str1 = '我是%s，今年%d岁了' % (name, age)
print('new_str1 = ' + new_str1)

# 字符串的格式化方法2
new_str2 = '我是{}，今年{}岁了'.format(name, age)
print('new_str2 = ' + new_str2)

# 有时候为了美观和便于检查
new_str3 = '我是{name}，今年{age}岁了'.format(
    name = 'python', age = 22
)
print('new_str3 + ' + new_str3)

# 最牛逼的方法是下面这种，是在Python3.6以后才有的
new_str4 = f'我是{name}，今年{age}岁了'
print('new_str4 = ' + new_str4)
