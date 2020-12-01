# 字典的访问与创建
a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}
# 只有不可改变的数据类型可以作为字典的键值，比如list就不能作为键值，但是tuple就可以。
print(a)

tuple1 = (1, 2, 3)
b = {
    1: 'a',
    tuple1: 'b',
    '3': 'c'
}
print(b)

# 当然还有别的方法
c = dict()
print(c)
d = dict(a = 1, b = 2, c = 'a')
print(d)

# 字典的访问
d = dict(a = 1, b = 2, c = 'a')
print('字典中键值c对应的元素是',d['c'])
print('''当k='b'时，对应的元素=''',d['b'])
# 注意字典和列表一样，是可以被改变的，所以字典不能成为另外一个字典的键值k
d['d'] = '123'
print(d)
d['c'] = 3
print(d)
