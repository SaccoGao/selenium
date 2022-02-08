import re
a = 'PythonC#JavaPHPC#,C#,C#'
# 把C#替换为GO
a1 = re.sub('C#', 'GO', a)
print(a1)

a2 = re.sub('C#', 'GO', a, count = 2) # 替换次数，默认为0，为0时不限制次数
print(a2)

# Python内置替换函数 replace
a3 = a.replace('C#','GO', 2)
print(a3)

# sub与Python函数
# 调用流程，sub方法查找C#，找到后，把C#作为参数传入sub_test内，并把函数的返回作为替换值
b = 'PythonC#JavaPHPC#,C#,C#'

def sub_test(value):  # 定义函数sub_test
    a = value.group()
    print(value)
    return '!'+ a +'!'

b1 = re.sub('C#', sub_test, b)  # 使用sub方法
print(b1)