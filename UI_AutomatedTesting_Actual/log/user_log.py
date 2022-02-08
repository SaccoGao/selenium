import logging
import os
import datetime

class UserLog:
    def __init__(self):
        # 实例化getLogger类
        self.logger = logging.getLogger()
        # 定义输出的日志级别
        self.logger.setLevel(logging.DEBUG)
        # 日志文件名
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, 'logs')
        log_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        log_file = log_dir + '/' + log_name
        # 控制台输出日志
        conlse = logging.StreamHandler()
        self.logger.addHandler(conlse)
        # 文件输出日志
        self.file_handle = logging.FileHandler(log_file, 'a', encoding = 'utf-8')
        formatter = logging.Formatter('%(asctime)s：%(filename)s-%(funcName)s %(levelno)s %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handel(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handel()