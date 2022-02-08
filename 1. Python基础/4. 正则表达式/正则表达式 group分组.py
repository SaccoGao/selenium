import re

s = 'life is short,i use python'
s1 = re.search('(life)\s(.*)\s(python)', s)
print(s1.group(0)) # 返回所有匹配的内容
print(s1.group(1)) # 返回分组1的内容
print(s1.group(2)) # 返回分组2的内容
print(s1.group(3)) # 返回分组3的内容
print(s1.group(1, 2, 3)) # 以元组的形式返回匹配组的内容
print(s1.groups()) # 以元组的形式返回匹配组的内容

s2 = re.findall('life(.*)python', s) #直接返回匹配组的内容
print(s2)