"""
定制类
"""

class Person(object):
    def __init__(self, name):
        self.name = name
        # fib的前两个值
        self.a, self.b = 0, 1

    # 定制对象的描述信息，print的时候显示的内容
    def __str__(self):
        return "Person Object (name: %s) " % self.name

    # 当前对象可以当作一个可迭代对象来使用
    # 对象变成可迭代对象， 必须返回一个迭代器
    def __iter__(self):
        return self

    # 把Person对象变成一个迭代器
    def __next__(self):
        self.a, self.b = self.b, (self.a + self.b)
        # 到达1000终止循环
        if self.a > 1000:
            raise StopIteration
        return self.a

    # 当前对象可以当作一个列表来使用
    # print(p[6])  # TypeError: 'Person' object is not subscriptable
    # 当前对象可以subscriptable，可以用下标引用特定的第几个值
    def __getitem__(self, item):  # item可能是个下标或者切片
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start if item.start else 0
            stop = item.stop if item.stop else -1
            a, b = 1, 1
            res_list = []
            for x in range(stop):
                if x >= start:
                    res_list.append(a)
                a, b = b, a + b
            return res_list

    # 调用属性值，如果函数中没有一个属性，就会调用这个函数，返回AttributeError
    # 如果想要避免AttributeError
    def __getattr__(self, item):
        """
        函数返回值
        """
        print("函数属性名字错误")
        if item == "location":
            return '北极'
        elif item == "eat":
            return lambda : print('eat函数执行，并且他不存在') # 返回一个函数，而不是None, 所以就不会报错了

    # 当前对象可以像函数一样使用
    # 一个对象的实例，可以像函数一样，拥有一个能被调用的能力
    # 这就说明，在python中，对象和函数的边界是不清晰的， 可以通过修改__call__把对象变成一个可以调用的函数
    def __call__(self):
        print("Person对象可以像函数一样被调用")



if __name__ == '__main__':
    p = Person("John")
    print(p)

    # 可迭代对象
    for n in p:
        print(n)

    # person既是一个可迭代对象，也是一个迭代器： 可以是一个列表
    # 下标
    print(p[6])  # TypeError: 'Person' object is not subscriptable --> 修改__getitem__()
    # 切片
    print(p[5:10]) # TypeError: 'slice' object cannot be interpreted as an integer

    # AttributeError: 'Person' object has no attribute 'location'
    print(p.location)
    # TypeError: 'NoneType' object is not callable 返回值为None不能被调用
    p.eat()
    # TypeError: 'Person' object is not callable 对象不能被当作函数一样调用
    p()
    # 判断一个对象是不是可以调用的对象， 可调用对象 == 函数
    print(callable(p))
