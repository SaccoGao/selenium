import configparser

class ReadIni:
    def __init__(self, load):
        self.data = self.load_ini(load)

    def load_ini(self, load):
        '''
        实例化ConfigParser
        :param load: 配置文件的绝对路径
        :return: 返回实例化的ConfigParser
        '''
        cf = configparser.ConfigParser()
        cf.read(load)
        return cf

    def get_value(self, key):
        '''
        读取配置文件下的配置
        :param element: 配置文件的section
        :param key: section下的key
        :return: 返回读取到的值
        '''
        return self.data.get('element', key)

readini = ReadIni('E:\Python_study\\UI_AutomatedTesting_Base\config\localElement.ini')
# uid = readini.get_value('element', 'username')
# pwd = readini.get_value('element', 'password')
# print(uid)
# print(pwd)

if __name__ == '__main__':
    read_ini = ReadIni('E:\Python_study\\UI_AutomatedTesting_Base\config\localElement.ini')
    print(read_ini.get_value('username'))


