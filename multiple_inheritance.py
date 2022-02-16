"""
多重继承的优先级
"""


class Father(object):
    def work(self):
        print("father is working")


class Mother(object):
    def work(self):
        print("mother is working")


class Child(Father, Mother):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    child1 = Child("小红")
    print(child1.work)

    # 继承是由优先级的
    # 按照优先级打印类的父结构/继承结构
    # 越往前优先级越高
    print(Child.__mro__)
