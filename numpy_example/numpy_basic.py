"""
numpu 基础
"""
import numpy as np

# 数组创建
l = [1, 2, 3, 4, 5]
arr = np.array(l)
print('数组创建', arr)

# 创建全0全1数组
array_zeros = np.zeros(10)
array_ones = np.ones(10)
array_full = np.full(shape=[2, 3], fill_value=2.557)
print('全0数组zeros', array_zeros)
print('全1数组ones', array_ones)
print('固定值数组full', array_full)

# 等差数列
array_range = np.arange(start=20, stop=50, step=3)
print('等差数列arange', array_range)
array_linespace = np.linspace(start=20, stop=21, num=10)
print('等差数列linspace', array_linespace)

# 随机整数
array_randint = np.random.randint(0, 10, size=5)
print('随机整数randint', array_randint)
# 正态分布
array_normalized = np.random.randn(10)
print('正态分布randn', array_normalized)
# 随机小数
array_float = np.random.random(size=5)
print('随机小数random.random', array_float)

# 查看操作
# 数组的轴数或维度
arr = np.random.randint(0, 100, size=(3, 4, 5))
dimension = np.ndim(arr)
print('数组的轴数或维度ndim', dimension)
# 数组的形状
shape = np.shape(arr)
print('数组的形状shape', shape)
# 数组的元素总数
size = np.size(arr)
print('数组的元素总数size', size)
# 数据类型
data_type = arr.dtype
print('数据类型array.dtype', data_type)
# 数组中每个元素大小
item_size = arr.itemsize
print('数组中每个元素大小array.itemsize', item_size)

# 文件IO操作
# 保存数组
arr1 = np.random.randint(0, 100, size=(3, 4, 5))
arr2 = np.random.randint(0, 100, size=(3, 4, 5))
# 文件名，保存的数据
np.save('data/data1', arr)
# 取出数据
arr3 = np.load('data/data1.npy')
print('读取数据load(.npy)', arr3)
# 存储多个
np.savez('data/data2.npz', number1=arr, number2=arr2)
# 读取一个数据
arr4 = np.load('data/data2.npz')['number1']
print('读取数据load(.npy)[data_name]', arr4)

# 数据类型: 整数 浮点数 字符串
# 整数
# int8 length 2**8 = [-128, 127]
arr_int8 = np.random.randint(-128, 128, size=(100, 50), dtype=np.int8)
print('int8 2**8 = [-128, 127]\n', arr_int8)

# uint8 length 2**8 = [0, 255]
arr_uint8 = np.random.randint(0, 256, size=(100, 50), dtype=np.uint8)
print('uint8 = [0, 255]\n', arr_uint8)

# int64 length 2**64
arr_int64 = np.random.randint(0, 100, size=(100, 50), dtype=np.int64)
# 数据类型不同会影响文件大小
np.save('data/data_int8', arr_int8)
np.save('data/data_int64', arr_int64)

# 转换数据类型，需要接收改变后的数组，不会修改原来的数组
print(arr_int8.dtype)
arr_float32 = arr_int8.astype(np.float32)
print(arr_float32)
print('\n')

# 数组运算
nd = np.random.randint(0, 10, size=(3, 5))
# 加减乘除直接算
print(nd + 5)
print(nd - 10)
print(nd * 2)
print(nd / 2)  # 除法
print(nd % 3)  # 取余
print(nd // 3)  # 整除
print(nd ** 3)  # 幂运算
# 逻辑运算
print(nd > 5)
print(nd == 5)
# 原始数据不会变，除非赋值
print(nd)

# *=、+=、-=操作, 没有/=
# 会修改现有数组，而不是创建一个新数组
nd += 3
print(nd)
nd -= 3
print(nd)
nd *= 3
print(nd)
print('\n')
# 复制（深复制）
arr = nd.copy()

# 索引和切片
arr_index = np.random.randint(0, 100, size=10)
print('原数据', arr_index)
print('单个元素索引array[x]', arr_index[3])
print('多个元素索引array[[x,y,z]]', arr_index[[0, 3, 5]])
print('切片array[from:to]', arr_index[3:9])
print('指定步长的切片array[from:to:step]', arr_index[3:9:2])
print('指定步长的切片array[from:to:step]', arr_index[::3])
print('指定步长的切片 - 负号表示倒序[::-1]', arr_index[::-1])
print('指定步长的切片 - 负号表示倒序[::-2]', arr_index[::-2])
# 切片赋值
arr_index[0:4:2] = 0
print('切片赋值array[from:to:step] = number', arr_index)

# 二维数组, 先去行，再取列
arr_index_2d = np.random.randint(0, 100, size=(5, 6))
print('原数据array2d\n', arr_index_2d)
print('单个元素索引array2d[row, column]', arr_index_2d[0, 3])
print('单个元素索引array2d[row][column]', arr_index_2d[0][3])
print('多个元素索引array2d[[row,row],[column,column]]', arr_index_2d[[0, 3], [2, 4]])
print('指定步长的切片array2d[row_from:to:step, column_from:to:step]\n', arr_index_2d[:4, 2:4])
print('索引和切片配合使用array2d[[row1,row2], column_from:to:step]\n', arr_index_2d[[1, 2], 2:4])
print('只取指定单独的几行几列, 先去所有行，再从行中取列\n array2d[[row1, row2]][:, [column1, column2, column3]]\n', arr_index_2d[[0, 2, 3]][:, [3, 4]])

#赋值操作
