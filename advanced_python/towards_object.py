import types

"""
面向对象的编程进阶
动态语言： 可以在运行过程中修改代码
静态语言： 编译时已经确定好代码，运行过程中不可以修改

为了限制class的属性的个数，使用__slots__变量来限制属性

@建筑研究 寇心雨
"""


# 没有限制属性的Person类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 限制属性的Person类
class PersonLimit(object):
    # 只允许当前类拥有name和age两个属性
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 限制属性的值：设置属性为私有属性，使用set和get方法
# 缺点： 有些人会直接添加一个age属性进去，造成麻烦
# 解决方法： 使用property
class PersonLimitRange(object):
    # age属性的额值限制为0-100岁
    def get_age(self):
        return self._age

    def set_age(self, value):
        if 0 <= value <= 100:
            self._age = value
        else:
            self._age = 0
            raise ValueError('age的值必须在0-100之间')

    def __init__(self, name, age):
        self.name = name
        self._age = age


# 使用property直接暴露类的属性
class PersonByProperty(object):
    @property
    def age(self):
        return self._age

    @age.setter  # 属性可以赋值
    def age(self, value):
        if 0 <= value <= 100:
            self._age = value
        else:
            self._age = 0
            raise ValueError('age的值必须在0-100之间')

    @property  # 没有settor不能修改初始值
    def name(self):
        self._name = '李四'
        return self._name


if __name__ == "__main__":
    p1 = Person('john', 23)
    # 1. 动态赋予对象p1一个对象属性
    p1.sex = 'male'
    # 2. 动态赋予类Person一个类属性
    Person.address = "北京"


    def run(self, work):
        print("%s正在完成的工作是%s" % (self.name, work))


    # 3. 动态赋予对象p1一个新的对象/成员/对象函数
    p1.run = types.MethodType(run, p1)
    p1.run('学习')


    # 4。动态赋予类Person一个新的类函数
    @classmethod
    def class_run(self, work):
        print("类函数中的class_run_method返回的是%s" % (work))
    Person.class_run_method = class_run
    p1.class_run_method('学习python')


    # 5.给Person类添加一个静态函数
    @staticmethod
    def static_run(work):
        print('静态函数返回的是%s' % (work))
    Person.static_run_method = static_run
    p1.static_run_method('学习面向对象的python')
    Person.static_run_method('学习全栈')

    """
    Limit class attributes
    """
    p2 = PersonLimit('john', 23)
    # 1. 动态赋予对象p1一个对象属性
    # p2.sex = 'male' # AttributeError: 'PersonLimit' object has no attribute 'sex'
    # 2. 动态赋予类Person一个类属性
    # Person.address = "北京" # AttributeError: 'PersonLimit' object has no attribute 'sex'

    """
    Property
    """
    p3 = PersonByProperty()
    p3.age = 80
    print(p3.name)
    print(p3.age)
