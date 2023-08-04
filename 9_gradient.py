import math
from numpy import *

def grad(a,b):
    n = a.shape[0]
    e = 0.000001
    i = 0
    
    
    x = zeros(n)
    x_copy= copy(x)
    delta = ones(n)
    alpha = 0
    r = 0
    
    while max(abs(delta)) > e:
        r = -(a.dot(x_copy)-b)
        a_r = a.dot(r)
        alpha = (r.dot(r))/(r.dot(a_r))
        x = x-(-r).dot(alpha) 
        delta = x_copy-x
        x_copy = copy(x)
        i+=1
    return x,i
    

a_data=([[10,2,1,1],
        [1,10,2,1],
        [1,1,10,1],
        [3,0,4,20]])

b_data=([10,12,8,17])

A = array(a_data,float)
B = array(b_data,float)
print('Ответ')
print(grad(A,B))
