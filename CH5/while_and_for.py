a = 5
while a > 0:
    print(a)
    a = a - 1

print('结束')

b = '12345'
c = [1, 2, 3, 4]
d = ['a', 'b', 'c', 'd']
e = {
    1: 'a',
    2: 'b',
    3: 'c'
}
for item in b:
    print(item)
for item in e.items():
    print(item)
for a, b in e.items():
    print('{}~~{}'.format(a,b))

set = {1, 2, 5, 4, 7}
for item in set:
    print(item)

for item in range(1,14,3):
    print(item)

