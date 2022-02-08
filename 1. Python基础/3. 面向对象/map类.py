list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
def square_1(x):
    return x*x

# 第一个参数为函数，第二个参数为列表，遍历列表中的元素，传入函数中
r1 = map(square_1, list_x)
print(list(r1))

r2 = map(lambda x, y: x+y, list_x, list_y)
print(list(r2))
'''
如果两个列表元素不一致
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6,]
多出来的元素不会被使用
'''