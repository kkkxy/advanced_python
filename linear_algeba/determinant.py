"""
行列式Determinant
一个矩阵必须是方阵才能计算行列式
把矩阵变成一个数字标量
numpy中有行列式的计算方式
行列式为0，不能计算逆矩阵
"""
import numpy as np

A = np.array([[1, 3],
              [3, 7]])
print(A)

det_a = np.linalg.det(A)
print(det_a)

B = np.random.randint(0, 10, size=(5,5))
print(B)

det_b = np.linalg.det(B)
print(det_b)
