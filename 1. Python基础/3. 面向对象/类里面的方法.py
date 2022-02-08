class Student():
    sum = 0
    name = ""
    age = ""

    ##构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
        ##print("打印构造函数")
        ##print(age)
        print(name + "加入班级")
        Student.plus_sum()

    ##类方法，6. 装饰器：@classmethod
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print("班级当前学生人数：" + str(cls.sum) + "\n")

    ##实例方法
    def do_homework(self):
        print(self.name + "做作业")

    def marking(self, score):
        if score < 0:
            self.score = 0
            print(self.name + "同学的分数是：" + str(self.score))
            return ("分数必须大于等于0")
        self.score = score
        print(self.name + "同学的分数是：" + str(self.score))

    ##静态方法
    @staticmethod
    def add(x, y):
        z = x + y
        print("This is tatic method:" + str(z))

Student1 = Student("高波", 18)
Student_Score = Student1.marking(score = -1)
print(Student_Score)

