"""
深度魔法！！！
元类 metaclass: 所有类的父类
先定义metaclass，就可以创建类，最后创建实例。
metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

@建筑研究 寇心雨
"""
"""
1. 使用import创建类
"""
# 引入模块，本质上，python解释器在引入模块时，使用type()函数创建了一个Person类
from metaclass import Person

# 测试
p = Person()
p.say('hello from .. import .. ')

# type()函数可以查看一个类型或变量的类型，Person是一个class，它的类型就是type，而p是一个实例，它的类型就是class Person
print(type(p)) # <class 'metaclass.Person'>
print(type(Person)) # <class 'type'>



"""
2. 使用type()创建类
type()函数既可以返回一个对象的类，又可以创建出新的类。
通过type()函数创建的类和直接写class是完全一样的。
要创建一个class对象，type()函数依次传入3个参数：
class = type(name=class name, bases=(inheritance_class1,), dict={method_name:function})
1. class的名称；
2. 继承的父类tuple，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；(object,)
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""
def func(self, words='hello'):
    print("I say %s" % words)
PersonByType = type('PersonByType', (object,), dict(say=func))

# 测试
p = PersonByType()
p.say('hello type class')
print(type(p)) # <class '__main__.PersonByType'>
print(type(Person)) # <class 'type'>

"""
3. 定义一个元类去创建类
所有的元类，一定要继承typ类。
"""
# 元类：类的模具
class MetaPerson(type):
    def __new__(cls, name, bases, attrs):
        def func(self, words='hello'):
            print("I say %s" % words)
        attrs['say'] = func
        return type.__new__(cls, name, bases, attrs)
# 根据上面的元类，创建一个Person类
class Person(object, metaclass=MetaPerson):
    pass

# 测试
p = Person()
p.say('hello')
print(type(p)) # <class '__main__.Person'>
# MetaPerson元类，type也是元类，不过tyoe是最顶级的元类，总之元类就是用来动态创建一个类的
# 打印创建Person类的元类，即为MetaPerson类，之前都是由type这个最顶级的元类创建的
print(type(Person)) # <class '__main__.MetaPerson'>
print(type(type(Person))) # <class 'type'>


"""
type是所有类的类型，他可以去创建所有的类，也就是所有类的父类
"""
print(int.__class__) # <class 'type'>
a = 123
print(a.__class__) # <class 'int'>
print(a.__class__.__class__) # <class 'type'>


