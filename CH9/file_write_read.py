# f = open()
# 'r': open for reading (default)
# 'w': open for writing, truncating the file first
# 'x': create a new file and open it for writing
# 'a': open for writing, appending to the end of the file if it exists
# 'b': binary mode
# 't': text mode (default)
# '+': open a disk file for updating (reading and writing)
# 接下去来展示不同的文件操作：
# f = open('test1.txt', mode = 'x')
# f.write('hello world')
# f.close()
#
# f = open('test2.txt', mode = 'x')
# f.write('hello world\n')
# f.close()

# f = open('test4.txt', mode = 'x')
# f.writelines(['123\n', 'helloworld\n', '[1, 2, 3]\n'])
# f.close()

f = open('test3.txt', mode = 'a')
f.writelines(['456\n', '789\n'])
f.close()

f = open('test4.txt', mode = 'w')
f.writelines(['456\n', '789\n'])
f.close()

# 怎么往文件里写入中文？
# 这是因为实际上python默认的仅仅只是支持Ascli码的写入，不能写中文。
# 方法就是需要引入open的另外一个属性：

f = open('test1.txt', mode = 'w', encoding = 'utf8')
f.writelines(['这样子就可以写中文了\n', '第三行\n'])
f.close()

# 接下去来说说文件读取的方法和步骤：
f = open('test1.txt', mode = 'r', encoding = 'utf8')
a = f. read()
print(a,type(a))
f.close()
# 这样子能读取，但是读取的是全部内容，但有时候我们并不想读取全部。
# 实际上我们有一种更加高效的读文件方法：
f = open('test1.txt', mode = 'r', encoding = 'utf8')
for line in f:
    print(line)
f.close()
# 这样子就能避免一次读取的文件太大的问题

# 还有别的方法吗？
f = open('test1.txt', mode = 'r', encoding = 'utf8')
b = f.readlines()
c = f.readline()
print(b,type(b))
print(c,type(c))
f.close()
# 所以说不推荐f.readlines
# 实际上在终端我们能够发现，f.readline每一次只读取文件的一行。





