list1 = [1,3,4,3,8,2,3,4,3]
print('list1的长度=',len(list1))
print('list1里的最大值是=',max(list1))
print('list1里的最小值是=',min(list1))

# 综合运用之前学习的字符串格式化方法
print('list1里面3这个元素共出现了{}次'.format(list1.count(3)))
print('lsit1里面3这个元素出现的次数=',list1.count(3))
m = list1.count(3)
print(f'list1里面3这个元素共出现了{m}次')
print('list1里面3这个元素共出现了%d次' %(m))

list2 = ['a', 'c', 'd']
print('list2=',list2)
list2.append('e')
print('list2_1=',list2)
list2.insert(1,'b')
print('list2_2=',list2)
list2.remove('d')
print('list2_3=',list2)

# 可以直接通过赋值语句改写list
list2[0] = 'x'
print('list2_4=',list2)

# 那么可以想像这种直接改写的方法对于字符串是不是也是适用的呢？
# a = 'abcde'
# print('a=',a)
# a[0] = 'x'
# print('a_1=',a)
# 会发现这是不行的，以上代码会报错

list3 = [1, 2, 3]
list4 = [3, 2, 1]
list3.reverse()
print('list3_1=',list3)
T = list3 == list4
print(T,type(T))

list5 = [1,3,4,3,8,2,3,4,3]
list5.sort()
print('list5_1=',list5)
list5.sort(reverse=True)
print('list5_2=',list5)

list6 = [1, 'abc', 1.3, ['a', 'b']]
print('list6=',list6)
list6.append('efg')
print('list6_1=',list6)
list6.insert(2,'hello,world')
print('list6_2=',list6)
list6.reverse()
print('list6_3=',list6)
list7 = ['efg', ['a','b'], 1.3, 'hello,world', 'abc', 1]
F = list6 == list7
print(F,type(F))

list8 = [1, 'abc', 7, 4, 'efg', 8, 10, 3, 'hij']
list8_1 = list8[0:1]
list8_1.extend(list8[2:4])
list8_1.extend(list8[5:8])
print('list8_1=',list8_1)
list8_1.sort(reverse=True)
print(list8_1)
list8_1.sort()
print(list8_1)



