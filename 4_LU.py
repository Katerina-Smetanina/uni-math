import math
from numpy import *

def LU(a, b):
    lu= matrix(zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]
    
    for k in range(n):
        for j in range(k, n):
            lu[k, j] = a[k, j] - (lu[k, :k] * lu[:k, j])
        for i in range(k + 1, n):
            lu[i, k] = (a[i, k] - (lu[i, : k] * lu[: k, k])) / lu[k, k]
    print(lu)
    
    y = zeros([lu.shape[0], 1])
    for i in range(y.shape[0]):
        y[i, 0] = b[i] - lu[i, :i] * y[:i]

    x = matrix(zeros([lu.shape[0], 1]))
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - lu[-i, -i:] * x[-i:, 0] )/ lu[-i, -i]

    return x

    

a_data=([[0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
        [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
        [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
        [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
        [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
        [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
        [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]])

b_data=([ 0.096,1.252,1.024,1.023,1.155,1.937,1.673])

A = array(a_data)
B = array(b_data)

set_printoptions(precision = 3)
print('Ответ',LU(A, B))