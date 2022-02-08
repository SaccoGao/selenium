import re

# 匹配字符串
a = 'c|c++|python|java|php'
a1 = re.findall('python', a)
print(a1)

# 匹配数字与非数字，使用元字符 \d  \D
b = 'c5c++6pytho\n 7java8php'
b1 = re.findall('\d', b)
print(b1)

b2 = re.findall('\D', b)
print(b2)

# 匹配单词字符，使用元字符 \w  \W
b3 = re.findall('\w', b)
print(b3)

# 字符集
c = 'abc, acc, adc, aec, afc, ahc'
c1 = re.findall('a[cf]c', c)
print(c1)
c2 = re.findall('a[^cf]c', c)
print(c2)



# 数量词 - 贪婪与非贪婪，正则表达式偏向于贪婪
d = 'python 1122java1122php'
d1 = re.findall('[a-z]{3,6}', d)
print(d1)
## 非贪婪
d2 = re.findall('[a-z]{3,6}?', d)
print(d2)

# * 匹配0次或者无限次
# + 匹配1次或者无限次
# ? 匹配0次或者1次
e = 'pytho0python1pythonn2'
e1 = re.findall('python*', e)
print(e1)
e2 = re.findall('python+', e)
print(e2)
e3 = re.findall('python?', e)
print(e3)

# 边界匹配
f = '123456789'
#要求匹配f是否在4-8位数
f1 = re.findall('\d{4-8}$', f)
print(f1)

# 匹配模式参数
g = 'PythonC#JavaPHP'
# re.I 忽略大小写
g1 = re.findall('c#', g, re.I)
print(g1)
# re.S

# . 匹配除换行符外，其他所有的字符


