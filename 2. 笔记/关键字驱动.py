import xlrd
from xlutils.copy import copy

# 1. 设计关键字模型（以excel文件为例）（具体文件见E:\Python_study\UI_AutomatedTesting_Actual\config\keyword.xls）

# 2. 往excel内写入数据
data = xlrd.open_workbook(excel_path) # 打开excel文件
write_data = copy(data) # 复制打开的excel文件
write_data.get_sheet(0).write(row, cell, value) # 在第一个sheet内的row行、cell列写入value，用于记录测试结果
write_data.save(excel_path)  # 保存文件
