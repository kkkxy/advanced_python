"""
正则表达式 Regular Expression
正则表达式是一种用来匹配字符串的强有力的武器。
它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

@建筑研究 寇心雨
"""
import re

# 通过正则表达式匹配多行字符串
tel_l = '''
aesdf
13811011234
aa1a3hi1233rhi3
87156340
affa124564531346546
afa19454132135
'''

# 匹配手机号
# 第二个数字是从3-9任意一个数字，{9}9个数字
pattern = re.compile(r'1[3,9]\d{9}')







