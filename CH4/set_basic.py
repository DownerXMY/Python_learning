set1 = {'a', 'b', 'c', 'd'}
print(set1, type(set1))
T = 'c' in set1
print(T,type(T))

list1 = [1, 2, 3, 1, 4, 2, 5, 2, 2]
# 如何去掉列表中所有重复的元素生成一个列表，运用集合会非常方便！
set2 = set(list1)
print(set2)
list1_1 = list(set2)
print(list1_1)
