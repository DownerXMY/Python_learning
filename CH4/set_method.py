# set1 = {'a', 'b', 'c', 'd'}
# print(set1)
# set1.add('e')
# print(set1)
# set1.remove('a')
# print(set1)
#
# # 如何通过字符串快速生成集合，元素取自字符串中不重复的项，而且是乱序的，这实际上标明集合是无序的数据类型。
# str1 = 'abcdefg'
# print(str1)
# set2 = set(str1)
# print(set2)
#
# str2 = 'aaabbbcccddd'
# print(str2)
# set2_1 = set(str2)
# print(set2_1)
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1 & set2)
# set10 = set1 | set2
# print(set10)
# print(set1 ^ set2)
# print(set1 - set2)

# 把所有可能的交集写入一个列表中
set1 = {1, 2, 3, 4, 9}
set2 = {1, 3, 4, 9 ,10}
set3 = {1 ,9, 11, 12}
set4 = {2, 4, 10, 11}

##############################
list1 = list(set1)
list2 = list(set2)
list3 = list(set3)
list4 = list(set4)

list_f = [list1, list2, list3, list4]
list_c = ['l1', 'l2', 'l3', 'l4']
org = []
for i in range(1,5,1):
    for item in range(1,len(list_f[i-1])+1,1):
        l = list_f[i-1]
        # print((list[i-1],l[item-1]))
        org.append([list_c[i-1], l[item-1]])
# print(org)

org1 = []
for j in range(1,13,1):
    org2 = []
    for l in range(1,len(org)+1,1):
        m = org[l-1]
        if m[1] == j:
            org2.append(m[0])
    org1.append(org2)
# print(org1)

org5 = []
for k in range(1,13,1):
    org4 = []
    org3 = [k]
    for p in range(k,13-k,1):
        if org1[p] == org1[k-1]:
            org3.append(p+1)
    # print(org1[k-1],org3)
    org4.append((org1[k-1], org3))
    org5.append((org1[k-1], org3))
    print(org4)
# print(org5)

set1 = {None}
inp = eval(input('请输入想要计算的集合'))
print(inp,type(inp),len(inp))
for r in range(1,13,1):
    s = org5[r-1]
    t = set(s[1])
    q = 1
    while q <= (len(inp)+1):
        q = q + 1
        if q > (len(inp)+1):
            break
        if inp[q-2] in s[0]:
            continue
        else:
            break
    if q == (len(inp)+2):
        set1 = set1 | t
    else:
        continue
set1 = set1 - {None}
print('所求集合的交集为：',set1)
#########################################