from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
'''
枚举类内常量的值无法更改
如运行：
VIP.YELLOW = 6
会报错，无法修改
'''

print(VIP.YELLOW)  # 打印结果为VIP.YELLOW，枚举类型
print(VIP.YELLOW.name) # 打印结果为YELLOW，枚举的名字
print(VIP.YELLOW.value)  # 打印结果为1，枚举的值

# 遍历枚举类，枚举类是可遍历的
for v in VIP:
    print(v)

# 枚举的比较运算
print(VIP.YELLOW == VIP.BLACK) # 运行进行相等比较，但是无法进行大小比较
print(VIP.YELLOW is VIP.BLACK) # is比较