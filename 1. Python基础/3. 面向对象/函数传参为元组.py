fgf = "~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def demo(param1, *param, param2 = "Sacco"):
    print("demo:")
    print("我是必须参数param1：" + param1)
    print("我是默认参数param2：" + str(param2))
    print("我是可变参数*param：" + str(param))
a = (1, 2, 3)
demo("Sacco", *a ,param2 = "Kava")


print(fgf)

def demo2(*param):
    print("demo2:")
    print(param)
demo2(1, 2, 3)

print(fgf)

c =50
def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()

func1()