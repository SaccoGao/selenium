import configparser

class ReadIni():
    def __init__(self, filename):
        self.data = self.load_ini(filename)

    def load_ini(self, filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    def get_value(self, section, key):
        return self.data.get(section, key)

readini_element = ReadIni('E:\\Python_study\\UI_AutomatedTesting_Actual\\config\\element.ini')

if __name__ == '__main__':
    readini_element = ReadIni('E:\\Python_study\\UI_AutomatedTesting_Actual\\config\\element.ini')
    a = readini_element.get_value('RegisterElement', 'username').split(',')
    print(a)