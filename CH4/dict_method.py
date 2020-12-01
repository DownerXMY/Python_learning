a = {
    'FA': 84,
    'MS': 80,
    'TSA': 95
}
b = ['浙江省','宁波市','鄞州区','常青藤小城']
c = ('Keanou', 'Tony', 'Danson')
d = {
    'name': 'Mingyue Xu',
    'age': 22,
    'school': 'SJTU',
    'major': 'math',
    'grades': a,
    'address': b,
    'friends': c
}

print(d)
print(d['name'])

print(d.get('name'))
print(d.get('none'))

print(d.keys())

print(d.values())

print(d.items())

d.pop('name')
print(d)
e = d.pop('age')
print(e)
print(d)

print(d.clear())

# 字典的更新
x = {
    1: 'a',
    2: 'b',
    3: 'c'
}
y = {
    '1': 'a',
    '2': 'b',
    '3': 'c'
}
print(x)
x.update(y)
print(x)
print(y)
y.update(x)
print(y)
# 如果两个字典中的k值有重复，那么更新会覆盖掉，比如
z = {
    1: 'abc',
    2: 'def'
}
x.update(z)
print(x)

# 最后介绍一种更加方便的办法
x = {
    1: 'a',
    2: 'b',
    3: 'c'
}
y = {
    '1': 'a',
    '2': 'b',
    '3': 'c'
}
z = {**x, **y}
print(x)
print(y)
print(z)
# z就相当于x.update(y)
