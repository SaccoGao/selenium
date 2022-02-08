# 闭包 = 函数+环境变量（函数定义时候）
def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve

f = curve_pre() # 调用函数curve_pre，return curve函数后，临时变量a应该被销毁
g = f(2) # 但是此处调用了返回curve函数，需要用到变量a，导致变量a一直存在，此为闭包
print(g)

# 函数调用链
def f1():
    a = 10
    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()

# 闭包实用实例
# 使用闭包解决
print('使用闭包解决'.center(12, '~'))
def Distance():
    Distance_traveled = 0 # 初始步数为0
    def Distance_new():
        Step_count = input('旅行者所走步数：')
        nonlocal Distance_traveled # 声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
        Current_istance = int(Distance_traveled) + int(Step_count)
        Distance_traveled = Current_istance
        print('旅行者走了'+str(Current_istance)+'步')
    return Distance_new

tourist = Distance()
tourist()
tourist()
tourist()

print('')
print("面向对象打印".center(12, '~'))

# 使用面向对象解决
class tourist():
    Distance_traveled = 0  # 初始步数为0

    def Distance_new(self):
        Step_count = input('旅行者所走步数：')
        Current_istance = int(self.Distance_traveled) + int(Step_count)
        print('旅行者走了' + str(Current_istance) + '步')
        return Current_istance

    @classmethod
    def Distance_travele_new(cls, Current_istance_class):
        cls.Distance_traveled = Current_istance_class

tourist_1 = tourist()
pos = tourist_1.Distance_travele_new(tourist_1.Distance_new())
pos = tourist_1.Distance_travele_new(tourist_1.Distance_new())
pos = tourist_1.Distance_travele_new(tourist_1.Distance_new())