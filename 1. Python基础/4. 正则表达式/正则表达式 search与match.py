import re
s = 'A8123B9'

# match 从字符串的第一个字符开始寻找，如果不符合，则返回空
s1 = re.match('\d', s)
print(s1)  # None

# 遍历整个字符串，返回找到的第一个结果
s2 = re.search('\d', s)
print(s2)

