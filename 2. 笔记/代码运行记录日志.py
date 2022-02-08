import logging # 日志模块

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) # 定义记录级别
'''
记录级别，从高到低，级别越低，记录的信息越多
CRITICAL
ERROR
WARNING 默认
INFO
DEBUG
NOTSET
'''

# 文件输出日志
file_handler = logging.FileHandler(path/xxx.log) # 输入到path/xxx.log
logger.addHandler(file_handler)

logger.debug('test')
file_handler.close()  # 关闭file_handler
logger.removeHandler(file_handler)  # 关闭logger