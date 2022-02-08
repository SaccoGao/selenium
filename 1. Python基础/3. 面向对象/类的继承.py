class Human():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)


class Student(Human):
    def do_homework(self):
        print('English Homework')


print(Student.sum)

Student1 = Student(name = '皮皮', age = 18)
print(Student1.name)
Student1.do_homework()