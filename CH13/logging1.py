# 日志记录
# debug(), info(), warning(), error(), critical()
# 一共有以上5中错误，级别依次提高。
# 注意这个文件的名字不能再去程logging了，否则调用的时候就会被覆盖，这个问题要时刻牢记，取文件名千万要当心！！！

import logging
format = '%(levelname)s:%(name)s:%(message)s'
# 但实际上format的格式可以很复杂，比如可以加时间,行数,函数名等等参数，可以上网查文档。
format1 = '%(asctime)s--%(funcName)s--%(lineno)d--%(levelname)s--%(name)s--%(message)s'
logging.basicConfig(filename = 'test_log', filemode = 'w', format = format1, level = 'ERROR')
def Myfunc():
    logging.debug('this is debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
    logging.critical('this is critical')

if __name__ == '__main__':
    Myfunc()

# 打印出来的只有下面三条日志，实际上这是因为我们系统有一个默认的错误级别，就是，所以只会WARNING，打印出来级别更高的。
# 当然我们有办法去改变这个默认级别，就是logging.basicConfig()
# 注意级别参数都必须是大写字母。
# 当然logging.basicConfig不止level这一个参数。
# 如果有了filename这个参数，那么日志将会往这个文件中以mode = 'a'去写入
# 那么我们当然还可以改变写入的模式，就要采用filemode这个参数
# 到目前为止我们看到的日志是类似以下这样格式的：
# INFO:root:this is info
# 那么实际上，格式也是可以自己设定和更改的。
# 我们可以先来看看默认的格式是什么样的：
print(logging.BASIC_FORMAT)
# 现在我们知道了：
# format = '%(levelname)s:%(name)s:%(message)s'

# 怎么获取自己的logging实例化对象？
logger = logging.getLogger('Mingyue_Xu')

# 注意这里的名字，原来系统默认是root，这个我们之前打印日志的时候就已经看到了。
def Myfunc1():
    logger.debug('this is debug!')
    logger.info('this is info!')
    logger.warning('this is warning!')
    logger.error('this is error!')
    logger.critical('this is critical!')

if __name__ == '__main__':
    Myfunc1()

# 注意这个时候虽然root已经全部被改成了Mingyue_Xu，但是格式依旧是logging这个类的format1，写入的文件依旧是test_log
# 实际上我们现在想做的事情就是，单独改变logger这个对象的这些属性，而不是说改变整个大类logging的属性
# 引入handler:
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('test1_log', mode = 'w')
c_handler.setLevel(logging.ERROR)
f_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(asctime)s--%(levelname)s--%(name)s--%(message)s')
f_format = logging.Formatter('%(funcName)s--%(levelname)s--%(name)s--%(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# c_handler是打到屏幕上的，f_handler是打到文件里的。
# 可以看到这里我们可以设置不同的级别，格式等等。
# 最后最关键的是要把这些handler赋给logger这个对象
logger.addHandler(c_handler)
logger.addHandler(f_handler)
# 操作还是比较复杂的。
# 这样以后，我们再去执行函数Myfunc1:
if __name__ == '__main__':
    Myfunc1()

# 最后还有一个问题，就是我们设置f_handler的级别是INFO，但是结果在文件test1_log里答应出来的只有ERROR以上的级别，这是为什么呢？
# 实际上我们说这和'父类与子类'是非常相似的，如果对象logger的级别比类logging的级别低，那么会按照大类的级别来。
# 所以绝大多数的时候，我们会把全局的level设置到最低，也就是DEBUG

# 最后一块内容，我们想看一下如何通过配置文件来设置logging
# 写在log_configuration中.

