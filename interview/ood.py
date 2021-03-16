class Student():
    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender
    def print_score(self):
        print('%s: %d' % (self.name, self.score))
    
    def get_gender(self):
        return self.__gender

    def get_grade(self):
        if self.score > 89:
            print('A')
        else:
            print('B')
    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('bad score')
    def __len__(self):
        return 10

lisa = Student('Jupyter', 55, 'f')
print(lisa._Student__gender)
lisa.print_score()
lisa.get_grade()
print(Student)
print(lisa)

class Teenger(Student):
    pass
ben = Teenger('Benben', 55, 'm')
print(ben.get_grade())
print(isinstance(ben,Teenger))
print(isinstance(ben,Student))
print(dir(ben))
print(getattr(ben, 'name'))
print(len(ben))


class Student2(object):
    count = 0

    def __init__(self, name):
        Student2.count += 1
        self.name = name

    def __del__(self):  # 在对象被删除时执行(在对象引用数降到0时执行)
        Student2.count -= 1


# 测试:
if Student2.count != 0:
    print('1测试失败!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('2测试失败!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('3测试失败!')
        else:
            print('Students:', Student2.count, lisa.count)
            print('4测试通过!')
ross = bart
print('aaa:', Student2.count)
del bart
print('Students:', Student2.count)
del lisa
print('Students:', Student2.count)
del ross
print('Students:', Student2.count)