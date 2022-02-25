"""
<面向函数的编程Functional Programming>
在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。
而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。
对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；
越高级的语言，越贴近计算，抽象程度高，执行效率低，比如python语言。
函数式编程的一个特点就是，[允许把函数本身作为参数传入另一个函数，还允许返回一个函数]
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

高阶函数 higher_order function
偏应用函数Partially Applied Functions
柯里化Currying
闭包Closure

@建筑研究 寇心雨
"""
import random
from functools import reduce

"""
<匿名函数>
lambda x: function
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
可以把匿名函数赋值给一个变量，再利用变量来调用该函数
可以把匿名函数作为返回值返回
"""
print("把匿名函数赋值给一个变量")
f = lambda x: x * x
print(f)
print(f(5))

print("把匿名函数作为返回值返回")


def build(x):
    return lambda: x * x


"""
<map函数> 
map(function, iterable) - > Iterator
"""
test_list = [1, 2, 3, 4, 5]
iterator1 = map(lambda x: x ^ 2, test_list)
list1 = list(iterator1)
print("map函数", iterator1, list1)


"""
<reduce函数>
reduce(function, Iterable, [可选：初始值initial value]) - > value
把一个可迭代对象中的每个元素进行聚合处理， 返回一个聚合之后的值。
不是标准库中的函数，需要从functools中调用
如果有初始值，会用初始值 + 第一个元素做聚合，如果没有初始值，会使用第一个和第二个元素做聚合。lambda中的x, y 即为这两个元素。
"""
# 通常用来做累加
test_list = [1, 2, 3, 4, 5]
add_all_numbers = reduce(lambda x, y: x + y, test_list)
print("累加", add_all_numbers)
# 求最大值
def getMax(a, b):
    if a > b:
        return a
    else:
        return b
print("求最大值", reduce(getMax, test_list))

"""
<filter函数>
filter(function, iterable) - > Iterator
把可迭代对象中的每一个元素根据函数做过滤操作，True留下，False扔掉
"""
def is_odd(n):
    return n % 2 == 1

new_list = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("filter过滤", new_list, list(new_list))


"""
<max函数，min函数，sorted函数>
(iterable1, iterable2, key=function) - > Iterator 
"""

"""
<返回函数的高阶函数>
"""
def get_sum(*args):
    def add():
        add_result = 0
        for n in args:
            add_result += n
        return add_result
    return add
res = get_sum(1,2,3,4,5)
print(res) # 函数本身
print(res()) # 调用函数之后的返回值

# 得到小于100的所有素数:
# 最小的质数为2， 除0，2之外的其他偶数都不是质数
# 思路 1.先得到所有大于1的奇数的生成器 2.把生成器中的所有元素过滤，去掉可以被小于该元素的质数整除的元素。
def odd_number():
    """
    得到所有大于1的奇数的生成器
    """
    n = 1
    while True:
        n += 2
        yield n

def has_redundant_value(x):
    """
    判断是否能够整除的函数，如果不能被整除，返回True
    """
    return lambda number: number % x > 0

def number_generator():
    """
    质数生成器
    """
    # 最小的质数是2
    yield 2
    # 所有大于1的奇数
    number_generator = odd_number()
    while True: # 死循环
        # 从生成器中拿到一个奇数x
        x = next(number_generator)
        # print(list(number_generator))
        # 以x为标准，过滤所有小于x的奇数，过滤之后再赋值给number_generator
        # filter返回的是一个可迭代对象，在number_generator中，边向后增加值，边去过滤这个值后面的所有值
        # 过滤后得到的是，对于小于等于当前值的每一个数，后面的值都没有他们的倍数值
        number_generator = filter(has_redundant_value(x), number_generator)
        yield x


# generator1 = odd_number()
# print(next(generator1))
# print(next(generator1))

# generator1 = number_generator()
# for n in range(20):
#     print(next(generator1))

"""
<Closure闭包>
一个函数定义中中引用了函数以外的函数，并且该函数可以在函数以外使用的函数。
适用于多层函数，有相互的因果关系。
"""
def first_function(a):
    """
    闭包的外部函数：
    1. 易定是一个高阶函数，返回一个函数
    """
    def second_function(b):
        """
        闭包的内嵌函数：
        1. 引入了second_function闭合范围以外的变量a（first_function的变量）
        2. 并且可以在函数定义环境之外执行
        """
        print("外部函数first_function参数 {}, 内嵌函数builtin function参数 {}".format(a, b))
        return a + b
    return second_function


# res = first_function(10)
# print(res(90))
# print(res(100))

"""
闭包的应用
设在oxy坐标系中存在一条直线：y = ax + b，给定:x, 求直线上的点P的纵坐标:y
1. 首先要知道是哪条线： a, b的值
2. 再去输入x求y
"""
def create_line(a: float, b: float):
    def line(x:float):
        return a * x + b
    return line

# line1 = create_line(2,3)
# line2 = create_line(1.5, -2)
# print("第一条直线: ", line1)
# print("第二条直线: ", line2)
# # 当x = 10时，两条直线上的点的y值
# y1 = line1(10)
# y2 = line2(10)
# print(y1, y2)

"""
闭包的需要注意的点:
1. 闭包内置函数里面修改外部函数变量的值
2. 闭包的陷阱
"""
# 闭包内置函数里面修改外部函数变量的值
def func1():
    # 外部函数中的值count，是一个介于全局变量和局部变量中的一种变量
    # nonlocal标识
    count =1
    def add():
        nonlocal count # 必须声明一个nonlocal标识，不然会报错
        print(count)
        count +=1
        return count
    return add
print(func1()()) # 报错


# 闭包的陷阱
def func2():
    function_list = []
    for i in range(1, 4):
        def func3():
            return i ** 2
        function_list.append(func3)
    return function_list
f1,f2,f3 = func2()
print(f1(), f2(), f3()) # 9 9 9
# 原因：执行顺序；for循环一步，然后初始化一个函数，全部循环完之后，我们再去调用所有函数，此时i已经循环到最后一个3了
# 在初始化三个函数f1, f2,f3时，没有任何初始化的值，然后当调用这三个函数时，i已经全部变成3了，所以返回值都是9
# 解决方法，让i的值变成初始化时就定义的变量，不受for循环影响

def func22():
    function_list = []
    for i in range(1, 4):
        def func33(_i=i): # 初始化函数的时候，就需要初始化_i, _i等于初始化时的i值
            return _i ** 2
        function_list.append(func33)
    return function_list
f1,f2,f3 = func22()
print(f1(), f2(), f3()) # 1 4 9

