"""
偏函数
把一个函数的某些值固定住，返回一个新函数，方便后面对于同一些参数的多次调用
@建筑研究 寇心雨
"""

# int默认按照十进制转换字符
import functools

print(int("123"))
# 16进制
print(int("123", base=16))
print(int("123", 16))

# 把字符串转换成十六进制
def int_16(num, base=16):
    return int(num, base=base)
print(int_16("123"))

# 使用functools生成偏函数
int_16 = functools.partial(int, base=16)
print(int_16("123"))