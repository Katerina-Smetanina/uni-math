import math
from numpy import *

def Gaussa(A):
    for k in range(A.shape[1]-1):
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
        for i in range (k + 1, A.shape[0]):
            nu = A[i,k]
            A[i] = A[i] - A[k] * nu
        print(A)
        
    arg = [A[A.shape[0] - 1, A.shape[1] - 1] / (A[A.shape[0] - 1, A.shape[1] - 2])]
    for i in range(A.shape[0] - 2, -1, -1):
        n = A[i,A.shape[1]-1]
        for j in range(len(arg)):
            n = n - arg[j] * A[i, A.shape[0] - 1 - j]
        arg.append(n)
        x = arg[::-1]
    return x
    
    
    
    
data=([2,-1,0,0],
      [-1,1,4,13],
      [1,2,3,14])


A = array(data,float)
print(Gaussa(A))

