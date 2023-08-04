import math
import copy
from numpy import *

def q(a):
    if a >= 0:
        return 1
    else:
        return -1

def QR(a,b):
    n = a.shape[0]

    for k in range(n):
        p = zeros(n)
        f = zeros(n)
        a_copy = zeros(a.shape)
        a_copy[:k][:] = a[:k][:]

        p[k]=a[k,k]+q(a[k,k])*sqrt(((a[k:,k])**2).sum())   
        for l in range(k+1,n):
            p[l]=a[l,k]
            
        for i in range(k,n):
            a_copy[k,k]= -q(a[k,k])*sqrt(((a[k:,k])**2).sum())
            
            for j in range(k+1, n):
                a_copy[i,j]=a[i,j]-2*p[i]*(((p[k:]*a[k:,j]).sum())/(((p[k:])**2).sum()))
                
        for i in range(n):
            f[i]=b[i]-2*p[i]*(((p[k:]*b[k:]).sum())/(((p[k:])**2).sum()))
            
        a = a_copy      
        b = f
        
    x = zeros(n)      
    for i in range(1,a.shape[0]+1):
        x[-i] = (b[-i] - (a[-i,-i:] * x[-i:]).sum())/a[-i,-i]        
    return x


if __name__ == "__main__": 
    a_data=([[0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
            [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
            [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
            [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
            [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
            [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
            [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]])

    b_data=([ 0.096,1.252,1.024,1.023,1.155,1.937,1.673])

    '''
    a_data=([[6.03,13,-17],
            [13,29,-38],
            [-17,-38,50.03]])

    b_data=([2.09,4.15,-5.11])
    '''
    A = array(a_data,float)
    B = array(b_data,float)
    set_printoptions(precision = 3)
    print('Answer:',)
    print(QR(A,B))
