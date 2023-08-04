import cmath
from numpy import *

def sq(a,b):
    t = zeros((a.shape), dtype = complex)
    n = a.shape[0]
    
    t[0,0] = sqrt(a[0,0])
    t[1:,0] = a[1:,0]/t[0,0]
    for i in range(1, n):
        t[i,i] = sqrt(a[i,i] - (t[i,:]**2).sum())
        
        for j in range(i+1, n):   
            t[j,i] = (a[j,i] - (t[i,:]*t[j,:]).sum())/t[i,i]
       
    t_trans = t.transpose()
    C = (t.dot(t_trans).real)
    print(C)
    
    y = zeros((n), dtype = complex)
    for i in range(0,n):
        y[i] = (b[i] - (t[i,:i] * y[:i]).sum())/t[i,i]
    
    x = zeros((n), dtype = complex)
    for i in range(1, n+1):
        x[-i] = (y[-i] - (t[-i:, -i] * x[-i:]).sum() )/ t[-i, -i]
        
    print (a.dot(x))
    return x
    
a_data=([2.2, 4, -3, 1.5, 0.6, 2, 0.7],
        [4, 3.2, 1.5, -0.7, -0.8, 3, 1],
        [-3, 1.5, 1.8, 0.9, 3, 2, 2],
        [1.5, -0.7, 0.9, 2.2, 4, 3, 1],
        [0.6, -0.8, 3, 4, 3.2, 0.6, 0.7],
        [2, 3, 2, 3, 0.6, 2.2, 4],
        [0.7, 1, 2, 1, 0.7, 4, 3.2])

b_data=([3.2, 4.3, -0.1, 3.5, 5.3, 9.0, 3.7])

A = array(a_data,complex)
B = array(b_data,complex)
set_printoptions(precision = 3)
print(sq(A,B).real)