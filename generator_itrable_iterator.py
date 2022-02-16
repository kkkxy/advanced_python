"""
可迭代(Iterable)、迭代器(Iterator)和生成器(Generator)
@建筑研究 寇心雨
"""
import os
import random
import time
from collections.abc import Iterable, Iterator, Generator

"""
<可迭代对象Iterable>
定义：一个可迭代的对象是实现了__iter__()方法的对象。
判断：isinstance(object, Iterable)
常见的可迭代对象：
    1）集合或者序列数据类型， list、tuple、set、dict、str(字符串是可迭代对象)
    2）文件对象
    3）在类中定义了__iter__()方法的对象，可以被认为是 Iterable对象，
        但自定义的可迭代对象要能在for循环中正确使用，就需要保证__iter__()实现必须是正确的（即可以通过内置iter()函数转成Iterator对象。
        iter()函数是能把Iterable转成Iterator对象，然后在for中使用。
例外：一个对象实现了__getitem__()方法可以通过iter()函数转成Iterator，即可以在for循环中使用，但它不是一个可迭代对象(可用isinstance方法检测())
"""
print("<可迭代对象Iterable>")
print(isinstance([], Iterable))  # true list 是可迭代的
print(isinstance({}, Iterable))  # true 字典是可迭代的
print(isinstance((), Iterable))  # true 元组是可迭代的
print(isinstance(set(), Iterable))  # true set是可迭代的
print(isinstance('', Iterable))  # true 字符串是可迭代的

currPath = os.path.dirname(os.path.abspath(__file__))
with open(currPath + '/test_files/model.py') as file:
    print(isinstance(file, Iterable))  # true

"""
<迭代器 Iterator>
定义：一个对象实现了__iter__()和__next__()方法，那么它就是一个迭代器对象。
判断：isinstance(object, Iterator)
分类：
    1. 集合和序列对象是可迭代的但不是迭代器
    2. 文件对象是迭代器
    3. 一个迭代器(Iterator)对象不仅可以在for循环中使用，还可以通过内置函数next()函数进行调用。
目标：
    节省内存空间，所以集合和序列不是迭代器，他们早已经存储了特定长度的序列了。
"""
print("<迭代器 Iterator>")
print(isinstance([], Iterator))  # false
print(isinstance({}, Iterator))  # false
print(isinstance((), Iterator))  # false
print(isinstance(set(), Iterator))  # false
print(isinstance('', Iterator))  # false

currPath = os.path.dirname(os.path.abspath(__file__))
with open(currPath + '/test_files/model.py') as file:
    print(isinstance(file, Iterator))  # true


"""
<生成器Generator>
定义: 一个生成器既是可迭代的Iterable也是迭代器Iterator。
判断: isinstance(object, Generator)
创建:
    1. 列表生成式
    2. 函数，关键字yield
遍历:
    1. 通过next来调用下一个元素（Error stopIteration）
    next(Generator)
    2. 或者通过for循环来遍历
    [i for i in generator]
    3. 通过object内置的__next__（Error stopIteration）
    generator.__next__
    4. 调用内置的send函数: 对于第一个值，必须用None作为参数，对于后面的值，加入的参数会打印在每次输出后面，打印成一行（Error stopIteration）
    generator.send(None)

"""
# 1、通过列表生成式来创建，通过next来调用下一个元素。或者通过for循环来遍历
# TIPS: 如果首先对generator next一下，游标位置已经往下走了一步，再进行for循环就会从第二个开始循环打印
# TIPS: next下一步没有值的时候会报错，但是for循环不会报错，所有优先使用for循环遍历
generator1 = (i for i in range(16) if i % 2 == 0)
print("通过列表生成式来创建生成器", generator1)
print(isinstance(generator1, Iterable))  # true
print(isinstance(generator1, Iterator))  # true
print(isinstance(generator1, Generator))  # true
print(hasattr(generator1, "__iter__"))  # true
print(hasattr(generator1, "__next__"))  # true

# 遍历
# 1) next(generator)
print(next(generator1))
print(next(generator1))
# 3) generator.__next__
print(generator1.__next__)
# 4) generator.send(param)
# 生成器的send(value)方法会将value值“发送”给生成器中的方法。value参数变成当前yield表达式的值。
# send()方法会返回生成器生成的下一个yield值或者StopIteration异常（如果生成器没有生成下一个yield值就退出了）。
# 当通过调用send()启动生成器时，value值必须为None，因为当前还没有yield表达式可以接收参数。
print(generator1.send(None))
# 2) for
for i in generator1:
    print(i)


# 2.通过函数来创建生成器，关键字yield
def gen():
    """
    顺序地返回[0,10)的之间的自然数
    """
    for i in range(10):
        if i % 2 == 0:
            yield i


generator1 = gen()
print("通过函数来创建生成器", generator1)
for i in generator1:
    print(i)


def fib_number(times):
    """
    特定次数的斐波那契数列
    """
    # 初始化前两个数字
    a, b = 1, 1
    n = 2
    print(a)
    print(b)
    while n < times:
        # a 等于原来的 b，b=原来的 a + 原来的 b
        a, b = b, (a + b)
        n += 1
        print(b)
    return "done"


# print("简单的fib数列 - 函数")
# fib_number(10)


def fib_number_generator(times):
    """
    特定次数的斐波那契数列
    """
    # 初始化前两个数字
    a, b = 1, 1
    n = 2
    while n < times:
        # 在函数中如果有yield关键字，函数返回的就是一个生成器，生成器里面的值是b的值
        yield b  # 返回b给生成器
        # a 等于原来的 b，b=原来的 a + 原来的 b
        a, b = b, (a + b)
        n += 1


# print("简单的fib数列 - 通过函数来创建生成器")
# generator1 = fib_number_generator(10)
# for i in generator1:
#     print(i)

def fib_number_infinity():
    """
    无限次生成斐波那契额数列的生成器
    :param times:
    :return:
    """
    # 初始化前两个数字
    a, b = 0, 1
    while True:
        yield b
        a, b = b, (a + b)


print("无限次fib数列 - 通过函数来创建生成器")
generator1 = fib_number_infinity()
for i in range(10):
    print(next(generator1))


def fib_number_infinity_temp():
    """
    无限次生成斐波那契额数列的生成器
    :param times:
    :return:
    """
    # 初始化前两个数字
    a, b = 0, 1
    while True:
        temp = yield b
        print(temp)  # 会输出None，因为yield b没有返回值
        a, b = b, (a + b)


print("无限次fib数列 - 通过函数来创建生成器 - 测试将yield b 返回值赋给temp")
generator1 = fib_number_infinity_temp()
for i in range(10):
    print(next(generator1))


def fib_number_infinity_send():
    """
    无限次生成斐波那契额数列的生成器
    :param times:
    :return:
    """
    # 初始化前两个数字
    a, b = 0, 1
    while True:
        # temp = yield b  # 输入的值会赋给temp
        # print(temp)
        b = yield b
        # a 等于原来的 b，b=原来的 a + 原来的 b
        a, b = b, (a + b)


print("无限次fib数列 - 通过函数来创建生成器 - 通过send传入函数执行前yield的值")
generator1 = fib_number_infinity_send()
print(generator1.send(None))  # 第一次初始化必须传入None
print(generator1.send(50))  # a = 50, b = 0 + 50
print(generator1.send(200))  # a = 200, b = 50 + 200
print(generator1.send(400))  # a = 400, b = 200 + 400


def fib_number_infinity_send_without_return_value():
    """
    无限次生成斐波那契额数列的生成器
    :param times:
    :return:
    """
    # 初始化前两个数字
    a, b = 0, 1
    while True:
        yield b  # 输入的值会影响yield初始值
        # a 等于原来的 b，b=原来的 a + 原来的 b
        a, b = b, (a + b)


print("无限次fib数列 - 通过函数来创建生成器 - 通过send和next")
generator1 = fib_number_infinity_send_without_return_value()
print(generator1.send(None))  # 第一次初始化必须传入None
print(generator1.send(50))
print(generator1.send(''))
print(generator1.send('123s'))
print(generator1.send(None))
print(next(generator1))
print(next(generator1))
print(next(generator1))

"""
协程模型
协程是一种用户态的轻量级线程，协程的调度完全由用户控制。
协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，
在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。
协程实现了CPU在两个函数之间进行切换从而实现并发的效果
"""


def system(c: Generator, times: int):
    """
    系统执行函数
    """
    n = 0
    while n < times:
        n += 1
        print('系统执行第{}次动作'.format(n))
        r = c.send(n)
        print('元素返回动作：{}'.format(r), '\n')


def element():
    """
    系统内的某一个元素执行函数
    """
    action_list = ['停止前进', '继续直行', '右转弯', '左转弯', '后退']
    r = ''
    while True:
        # send yield传入当前次数n
        n = yield r
        if not n:
           return
        print('元素执行第{}次动作 '.format(n))
        r = random.choice(action_list)


# 定义一个系统元素
c = element()
# 启动跟随者
print(next(c))
# 运行系统
system(c, 5)
