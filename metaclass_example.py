"""
例子： 动态修改所有类属性的名字为大写
@建筑研究 寇心雨
"""
"""
方法一，定义返回元类的函数实现
"""
def upper_attr(class_name, class_parents, class_attrs):
    """
    遍历任何一个类中所有的类属性，把所有非私有的属性改成大写的
    定义一个字典，保存所有改完的属性的集合
    """
    new_attrs = {}
    for name, value in class_attrs.items():
        # 过滤掉私有属性
        if not name.startswith('__'):
            new_attrs[name.upper()] = value
        # 直接调用tyoe新建一个类
    return type(class_name, class_parents, new_attrs)

# 测试
# upper_attr的功能类似type，本质上就是创建一个元类，所以这里直接把函数upper_attr传入metaclass
class Example1(object, metaclass=upper_attr):
    # 类属性 class_attrs
    name = "xiaowang"
    acl = 1000


"""
方法二： 自定义Metaclass实现
"""
class UpperMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attrs):
        new_attrs = {}
        for name, value in class_attrs.items():
            # 过滤掉私有属性
            if not name.startswith('__'):
                new_attrs[name.upper()] = value
            # 直接调用tyoe新建一个类
        return type.__new__(cls, class_name, class_parents, new_attrs)

# 测试
# upper_attr的功能类似type，本质上就是创建一个元类，所以这里直接把函数upper_attr传入metaclass
class Example2(object, metaclass=UpperMetaClass):
    # 类属性 class_attrs
    name = "xiaowang"
    acl = 1000


if __name__ == '__main__':
    # 判断Emp中是否有name的类属性
    print(hasattr(Example1, 'name'))
    print(hasattr(Example1, 'acl'))
    # 判断Emp中是否有NAME的类属性
    print(hasattr(Example1, 'NAME'))
    print(hasattr(Example1, 'ACL'))

    # 判断Emp中是否有name的类属性
    print(hasattr(Example2, 'name'))
    print(hasattr(Example2, 'acl'))
    # 判断Emp中是否有NAME的类属性
    print(hasattr(Example2, 'NAME'))
    print(hasattr(Example2, 'ACL'))


