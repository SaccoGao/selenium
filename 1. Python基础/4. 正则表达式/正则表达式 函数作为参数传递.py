import re
s = 'A8C3721D86'

# 把变量s中，大于等于6的数字替换为9，小于6的数字替换为0

def convert(value):
    match = value.group()
    match = int(match)
    print(match)
    if match >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)
print(r)