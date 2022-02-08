from functools import reduce

# 连续计算，连续调用lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x+y, list_x) # reduce函数，传入的函数中必须有两个参数
print(r)

list_xy = [(1,2), (2,-2), (-1,4)]
a = reduce(lambda x, y: x+y , (0,0))
print(a)