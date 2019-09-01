# 自醒是通过一定的机制查询到对象的内部结构


class Person:
    name = "User"


class Student(Person):
    def __init__(self, school_name=''):
        self.school_name = school_name



user = Student("慕课网")
print(user.__dict__)
print(user.name)
