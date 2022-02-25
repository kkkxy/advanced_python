"""
逆矩阵
XW = Y
X-1 X W = X-1 Y
I W = X-1 Y
W = X-1 Y
"""
import numpy as np

# 三元一次方程
# 3 * w1 + 2 * w2 + 4 * w3 = 19
# 2 * w1 - 1 * w2 + 3 * w3 = 9
# 1 * w1 + 1 * w2 - 1 * w3 = 0

X = np.array([[3, 2, 4],
             [2, -1, 3],
             [1, 1, -1]])
Y = np.array([19, 9, 0])

print(X, Y)
# X的逆矩阵
X_1 = np.linalg.inv(X)
W = X_1.dot(Y)
print(W)

"""
逆矩阵相关公式
(A B)-1 = B-1 A-1
(A-1)-1 = A
(AT)-1 = (A-1)T
"""


