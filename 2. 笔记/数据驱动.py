import ddt
import xlrd

# 数据驱动 - 使用ddt标准库
@ddt.ddt # 继承ddt标准库
class LoginTest():
    @ddt.data([1, 2], [3, 4])
    @ddt.unpack # 解包
    def test_login_succees(self, a, b):
        result = a + b
        print(result) # 方法会执行两次，分别为：1+2、3+4
# ddt标准库会把data内列表参数，依次传入方法中

# 使用ddt标准库，传入excel内的参数
# 操作excel文件，使用xlrd
data = xlrd.open_workbook(excel_path) # 打开excel文件
table = self.data.sheets()[index] # 获取sheet
rows = self.table.nrows # 获取有效行数
table.row_values(i) # 获取excel文件的sheet内第i行的内容，以列表的形式返回

# excel+ddt实现数据驱动
data = [[1,2], [3,4]] # 可从excel内读取，实例见UI_AutomatedTesting_Actual -> util -> excel_util块
@ddt.ddt
class LoginTest():
    @ddt.data(*data)
    def test_login_succees(self, data): # 传入data参数
        a,b = data # 把data内的[1,2]、[3,4]，分两次执行，分别赋值给a和b
        result = a + b
        print(result) # 方法会执行两次，分别为：1+2、3+4