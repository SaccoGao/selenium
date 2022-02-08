import xlrd
import xlwt

# 获取xls文件
wb = xlrd.open_workbook('D:\shipfundList.xls')

# 打开第一张表
table = wb.sheets()[0]

# 获取表的行数
nrows = table.nrows

for i in range(nrows): # 循环逐行打印
    if i == 0:# 跳过第一行
        continue
    print (table.row_values(i)[:2]) # 取前十三列