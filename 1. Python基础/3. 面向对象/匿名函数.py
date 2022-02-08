# 普通函数
def add(x, y):
    return x+y

print(add(1, 2))

# 以匿名函数的方式表示普通函数，匿名函数后面只能跟表达式
f = lambda x, y: x+y
print(f(1, 2))

# 三元表达式，相当于普通语句的if判断
'''
实例：n与m行比较，返回值大的一方
三元表达式写法：条件为真时返回的结果 if 判断条件 else 条件为假时返回的结果
'''
r = lambda n, m: n if n>m else m
r1 = r(1, 2)
print(r1)