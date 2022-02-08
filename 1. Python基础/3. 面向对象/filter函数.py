# 过滤不符合条件的元素
list_x = [1, 0, 0, 1, 0]
r = filter(lambda x: True if x == 1 else False, list_x)
print(list(r))

list_u = ['a', 'B', 'c', 'D', 'E']
a = filter(lambda u: True if u.islower() else False, list_u)
print(list(a))