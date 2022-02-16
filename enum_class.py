"""
枚举类
枚举的值自动从1开始且不会重复
"""
from enum import Enum

# 1. 直接定义
Month = Enum('title - month', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
print(Month.__members__)

# 二月份的值
print(Month['feb'].value)
# 根据值得到名字
print(Month(2).name)

# 2. 用类去定义
class Color(Enum):
    """
    枚举类中不允许数字的值相同， 如果有重复，根据value取name只能得到第一个name
    """
    red = 100
    green = 200
    blue = 300

print( Color(200))