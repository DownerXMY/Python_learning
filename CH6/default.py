# 参数的默认值
# 参数的默认值必须放到最后一位
def test(a, b = False):
    if b:
        return a
    else:
        return a * a
print(test(a = 2))

def test_1(a, b = True):
    if b:
        return a
    else:
        return a * a
print(test_1(a = 2))
