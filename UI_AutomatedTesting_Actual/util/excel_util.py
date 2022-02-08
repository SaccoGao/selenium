# coding = utf-8
import xlrd
from xlutils.copy import copy

class ExcelUtil():
    def __init__(self, excel_path = None, index = None):
        if excel_path == None:
            excel_path = 'E:\\Python_study\\UI_AutomatedTesting_Actual\\config\\casedata.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    def get_data(self):
        '''
        获取excel数据
        :return: list
        '''
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    def get_lines(self):
        '''
        获取行数
        :return:
        '''
        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            return None

    def get_col_value(self, row, cell):
        if self.get_lines() > row:
            data = self.table.cell(row, cell).value
            return data
        else:
            return None

    def write_value(self, row, value):
        read_value = self.data
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 7, value)
        write_data.save('E:\\Python_study\\UI_AutomatedTesting_Actual\\config\\keyword.xls')

if __name__ == '__main__':
    ex = ExcelUtil('E:\\Python_study\\UI_AutomatedTesting_Actual\\config\\keyword.xls')
    print(ex.write_value(7, '帅气逼人皮皮波'))