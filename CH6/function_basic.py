a = [1, 2, 3, 4, 5]
print(max(a))

# 实际上我们早就已经应用了函数，下面我们写成函数的专业形式
def demo():
    print('hello world')
    print('embrace the world')

demo()

def demo1(a, b):
    print(a, b)

demo1(a = [1, 2, 3], b = {
    1: 1,
    2: 2
})

def sum(a, b):
    return a + b

print(sum(1, 2))
# print(sum(1, '2'))
print(sum([1, 2, 3], [4, 5, 6]))
print(sum(b = [1, 2, 3], a = [4, 5 ,6]))

def minemax(a):
    if not a:
        return None
    max_value = 0
    for i in range(1,len(a)+1,1):
        if max_value < a[i-1]:
            max_value = a[i-1]
        else:
            continue
    return max_value

list = eval(input('请输入一个列表：'))
print(minemax(list))



