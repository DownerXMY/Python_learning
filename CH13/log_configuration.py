import logging

# print(logging.BASIC_FORMAT)
format_new = '%(asctime)s~~%(levelname)s~~%(name)s~~%(message)s'
logging.basicConfig(filename = 'log_conf', filemode = 'w', format = format_new, level = 'DEBUG')
def Function1():
    logging.debug('Discover DEBUG')
    logging.info('Discover INFO')
    logging.warning('Discover WARNING')
    logging.error('Discover ERROR')
    logging.critical('Discover CRITICAL')
if __name__ == '__main__':
    Function1()

logger = logging.getLogger('Have a nice day!')
f_handler = logging.FileHandler('logf_conf', mode = 'w')
f_handler.setLevel('WARNING')
f_handler.setFormatter(logging.Formatter('%(asctime)s~~%(funcName)s~~%(name)s~~%(message)s'))
logger.addHandler(f_handler)
def Function2():
    logger.debug('Discover DEBUG')
    logger.info('Discover INFO')
    logger.warning('Discover WARNING')
    logger.error('Discover ERROR')
    logger.critical('Discover CRITICAL')
if __name__ == '__main__':
    Function2()

# 那么怎么用配置文件来设置一个日志的属性呢？
# 注意我们要写的是一个.conf文件
# 那么怎么创建配置文件呢？实际上需要引入模块

from logging.config import fileConfig
fileConfig('logger1.conf')
logger1 = logging.getLogger('Set Attributes By Conf')
logger1.warning('unexpected warning!')
# 这样，我们就成功运用配置文件设置了一条日志。


