import math
from numpy import *

def Gaussa(A):
    for k in range(A.shape[0]):
        max_value_colomn = 0
        str = 0
        
        for i in range (k, A.shape[0]):
            if abs(A[i,k]) > abs(max_value_colomn):
                max_value_colomn = A[i,k]
                str = i
                
            if max_value_colomn == 0:
                print('я выродился')
                break    
                
        buff = repeat(A[k], 1)
        A[k], A[str] = A[str], buff

        A[k] = A[k] / max_value_colomn
        for i in range(0, A.shape[1]-1):
           if i != k:
               nu = A[i,k]
               A[i] = A[i] - A[k] * nu
    print(A)
    return A[:,-1]
            
data=([0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245, 0.096],
      [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101, 1.252],
      [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321, 1.024],
      [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183, 1.023],
      [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423, 1.155],
      [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923, 1.937],
      [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105, 1.673])

A = array(data)
print(Gaussa(A))           