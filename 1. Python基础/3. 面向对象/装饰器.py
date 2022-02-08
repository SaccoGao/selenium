import time
# 增加打印时间
def f1():
    print(time.time()) # 增加打印时间的方法
    # unix 时间戳
    print('This is a function')

f1()

# 装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def f2():
    print('This is a function')

# 往函数内增加打印时间的功能
# 方法1
print('\n方法1打印：')
f = decorator(f2) # 在函数decorator内传入函数f2，返回函数wrapper
f() #调用返回的wrapper函数

#方法2
@decorator  # 增加装饰器
def f2():
    print('This is a function')

print('\n方法2打印:')
f2()

print('\n装饰器带有参数：')
# 被装饰的函数有参数
# 一个参数
def decorator_1(func):
    def wrapper_1(*args):
        print(args)
        print(time.time())
        func(*args)
    return wrapper_1

@decorator_1
def f3(func_name): # 此处有参数，需要在装饰器处加上对应的参数
    print('This is a function' + func_name + '\n')

f3('test func_name')

@decorator_1
def f4(func_name_1, func_name_2):
    print('This is a function' + func_name_1 + func_name_2 + '\n')


f4('func_name_1', 'func_name_2')