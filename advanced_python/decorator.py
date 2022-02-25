"""
装饰器
@建筑研究 寇心雨
"""
import time
from functools import wraps

"""
例子
"""
def eat():
    print('我在吃饭')

def func1(function):
    """
    高阶函数，把函数作为参数传入
    其他边边角角的功能
    """
    def func2():
        print('给你把饭做好')
        function()
        print('洗碗')
    return func2
today_eat = func1(eat)
today_eat()
print('\n')

"""
<装饰器decorator>
给某个已经存在的函数添加额外的功能
"""

def func1(function):
    """
    高阶函数，把函数作为参数传入
    其他边边角角的功能
    """
    def func2():
        print('给你把饭做好')
        function()
        print('洗碗')
    return func2

@func1 #装饰器
def eat():
    print('我在吃饭')

eat()
print(eat.__name__)
print('\n')
# 实际上eat函数就是func2函数， 所以这里打印出的函数名字是func2而不是eat

"""
一般来说，
我们不想造成误会，希望调用eat函数时，就指的是当前的核心函数eat：
引入wraps，对func2进行包装
"""

def func1(function):
    """
    高阶函数，把函数作为参数传入
    其他边边角角的功能
    """
    @wraps(function) # 使用function来包装func2
    def func2():
        print('给你把饭做好')
        function()
        print('洗碗')
    return func2

@func1 #装饰器
def eat():
    print('我在吃饭')

eat()
print(eat.__name__)
print('\n')


"""
使用装饰器给work函数增加记录日志上的功能
"""
def logger(function):
    @wraps(function)
    def write_logs():
        print("info -- time: {}".format(time.strftime('%H:%M:%S'), time.localtime()))
        function()
    return write_logs

@logger # 使用装饰器给所有的work增加记录日志上的功能
def work():
    print("我在工作")
    return

work()
time.sleep(1)
work()


"""
带参装饰器
"""
@logger
def work2(name):
    print("{}在工作".format(name))

# work2("John")
# TypeError: work2() missing 1 required positional argument: 'name'
# work2可能有参数，装饰器中会报错


"""
1. 核心函数中可能有多个参数，需要传入装饰器
2. 装饰器中需要其他的参数，比如记录日志的级别
"""
# 核心函数中可能有多个参数
def logger4(function):
    @wraps(function)
    def write_logs(*args, **kwargs): # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
        print("info -- time: {}".format(time.strftime('%H:%M:%S'), time.localtime()))
        function(*args, **kwargs) # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
    return write_logs

@logger4
def work2(name):
    print("{}在工作".format(name))

def work3(name1, name2):
    print("{}和{}在工作".format(name1, name2))

work2("小明")
work3("张三", "李四")

# 装饰器中需要其他的参数：传入文件名字
# 再加一层嵌套的函数
def main_logger(log_file='out.log'):
    def logger(function):
        @wraps(function)
        def write_logs(*args, **kwargs):  # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
            log = "[info] -- time: {}".format(time.strftime('%H:%M:%S'), time.localtime())
            print(log)
            with open('test_files/' + log_file, 'a') as f:
                f.write(log + '\n')
            function(*args, **kwargs)  # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
        return write_logs
    return logger

@main_logger('work2.log')
def work2(name):
    print("{}在工作".format(name))

work2("小白")
work2("小兰")


"""
使用一个类来创建装饰器
"""
class Logs(object):
    def __init__(self, log_file='out.log', level='info'):
        self.log_file = log_file
        self.level = level
    def __call__(self, function):
        """
        用来声明接收函数，定义装饰器
        需要有一个接收函数
        """
        @wraps(function)
        def write_logs(*args, **kwargs):  # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
            log = "[{}] -- time: {}".format(self.level, time.strftime('%H:%M:%S'), time.localtime())
            print(log)
            with open('test_files/' + self.log_file, 'a') as f:
                f.write(log + '\n')
            function(*args, **kwargs)  # 在这里添加： *args 多个参数 **kwargs 多个关键字参数
        return write_logs


@Logs('work2.log', level='WARNING')
def work3(name):
    print("{}在工作".format(name))

work3("小白")















