import copy
import time

'''
1. 深浅拷贝
'''
# 可变数据类型
a1 = ['s1', 's2', 's3']
a = [1, 2, 3, 4, a1]
b = copy.copy(a)  # 浅拷贝，只是拷贝了列表，而没有深入到内部的子对象，拷贝后的内容一致，但是内存地址不同
c = copy.deepcopy(a)  # 深拷贝，深入到内部的子对象进行拷贝，拷贝后的内容一致，但是内存地址不同
print(a,":",id(a))  # [1, 2, 3, 4, ['s1', 's2', 's3']] : 内存地址a
print(b,":",id(b))  # [1, 2, 3, 4, ['s1', 's2', 's3']] : 内存地址b
print(c,":",id(c))  # [1, 2, 3, 4, ['s1', 's2', 's3']] : 内存地址c
a1.append('s4') # 修改a1的值，证明浅拷贝未拷贝内层对象
print(a,":",id(a))  # [1, 2, 3, 4, ['s1', 's2', 's3', 's4']] : 内存地址a
print(b,":",id(b))  # [1, 2, 3, 4, ['s1', 's2', 's3', 's4']] : 内存地址b，变量b只是拷贝了外部列表，内部保持一致
print(c,":",id(c))  # [1, 2, 3, 4, ['s1', 's2', 's3']] : 内存地址c

# 不可变数据类型
d = (1, 2, 3, 4)
e = copy.copy(d)  # 浅拷贝，只是拷贝了列表，而没有深入到内部的子对象，拷贝后的内容一致，内存地址一致
f = copy.deepcopy(d)  # 深拷贝，深入到内部的子对象进行拷贝，拷贝后的内容一致，但是内存地址不同
print(d,":",id(d))  # [1, 2, 3, 4] : 内存地址d
print(e,":",id(e))  # [1, 2, 3, 4] : 内存地址d
print(f,":",id(f))  # [1, 2, 3, 4] : 内存地址c
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
2. 装饰器（在不改变函数本身的前提下，增加新功能，内容：装饰器语法）
要求不改变run韩式，运行run函数时打印当前时间
'''
# 装饰器语法
def run_time(func):
    def get_time(*args):
        print(time.time())
        func(*args)
    return get_time
# 增加装饰器
@run_time
def run(stdent):
    print(stdent)
# 执行韩式
run('张三')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
3. return和yield的区别
'''
def func1():
    for i in range(1, 5):
        return i

def func2():
    for i in range(1, 5):
        yield i

print(func1())  # return终止了循环，返回了1
print(func2())  # yield不会终止循环，而是把遍历的数据装到一个对象内进行返回
for i in func2():
    print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
4. 推导式
根据list1，创建一个新list，list内的数字，都是list1内数字的平方
'''
list1 = [1, 2, 3, 4, 5]
list2 = list(map(lambda x:x*x, list1))  # 使用lambda表达式实现（匿名函数）
list3 = [x*x for x in list1]  # 使用推导式实现（列表推导式），[x*x for x in list1 if x>2]后面可加过滤条件
print(list1)
print(list2)
print(list3)

# 额外内容：字典推导式
my_json = {'key1':10, 'key2':20, 'key3':30}
keys = [key for key,value in my_json.items()]  # 取出字典中的key
values = [value for key,value in my_json.items()]  # 取出字典中的value
my_json_1 = {value : key for key,value in my_json.items()}  # key和value颠倒
print(keys)
print(values)
print(my_json_1)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
5. 算法：冒泡排序及快排
'''
# 冒泡排序
def bubble_sort(list):
    count = len(list)
    if count <=0:
        return []
    else:
        for i in range(0, count):
            for j in range(i+1, count):
                if list[i] > list[j]:
                    list[i],list[j] = list[j],list[i]
        return list
a = [99, 11, 77, 11, 66, 88]
result_bubble = bubble_sort(a)
print(result_bubble)

# 快排
def quick_sort(list):
    if list == []:
        return []
    else:
        first = list[0]
        # 推导式实现
        less = quick_sort([l for l in list[1:] if l < first])
        more = quick_sort([m for m in list[1:] if m >=first])
        return less + [first] + more
b = [99, 11, 77, 11, 66, 88]
resule_quick = quick_sort(b)
print(resule_quick)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
6. 如何理解面向对象及面向对象的特点
理解：编程世界对现实世界的一种延伸，用编程语言描述物体
特点：封装、继承、多态
'''
# 封装
class Animal:  # 封装了一个动物类，动物具有跑、吃、说话特征
    def run(self):
        print('Animal run')

    def eat(self):
        print('Animal eat')

    def talk(self):
        print('Animal talk')
a = Animal()
a.eat()

# 继承
class Human(Animal):  # 定义了一个Human类，继承了Animal类的特性，也具有跑、吃、说话特征，同时能自行封装其他特征
    def study(self):
        print('Human study')

h = Human()
h.eat()
h.study()

# 多态
class Dog(Animal):  # 同一个方法talk，不同的子类有不同的形态
    def talk(self):
        print('Dog talk')
d = Dog()
d.talk()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
7. 类中的私有变量能否访问，如果能，如何访问
能访问，当类里面有变量被定义未私有变量（__），放稳时可以在前面加 _类名
'''
class Student:
    __name = '三毛'
    school = '北大'
print(Student._Student__name)  # 访问私有变量
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
8. python中的类，有多少种方法种类，区别是什么
'''
class Human:
    def eat(self):  # 实例方法，实例可以操作的方法，可以操作实例变量，类无法直接调用
        print('吃东西')

    @classmethod
    def run(cls):  # 类方法，类可以直接调用，类方法可以操作类变量
        print('跑步')

    @staticmethod
    def sleep():  # 静态方法，脱离了类而存在
        print('睡觉')

'''
9. 用函数实现过滤list1中的空格和空值
'''
list1 = ['', 'hello', None, 'python']
result_list1 = [x for x in list1 if x != '']
result_list1 = [x for x in result_list1 if x != None]
print(result_list1)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

'''
10. 用函数实现计算集合list2中，所有元素的和
'''
list2 = [1, 2, 3, 4, 5]
resule_list2 = sum(list2)
print(resule_list2)