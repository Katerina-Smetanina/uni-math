import math
from numpy import *

def relax(a,b):
    n = a.shape[0]
    e = 0.000001
    omega = 1.4
    i = 0
    
    
    for k in range(n):
        b[k] = b[k]/a[k,k]
        a[k]=a[k]/a[k,k]

    x = zeros(n)
    x_copy= copy(x)
    delta = ones(n)

    while max(abs(delta)) > e:
        x_copy = copy(x)
        for k in range(n):           
            sum=0
            for j in range(n):                
                if j!=k:
                     sum =sum + x[j]*a[k,j]
            x[k]=(1-omega)*x[k]+omega*(b[k]-sum)
        print(x)
        delta = x_copy-x
        i+=1
        
    return x,i
    
def zeidal(a,b):
    n = a.shape[0]
    e = 0.000001
    i = 0
    
    for k in range(n):
        b[k] = b[k]/a[k,k]
        a[k]=a[k]/a[k,k]

    x = zeros(n)
    x_copy= copy(x)
    delta = ones(n)

    while max(abs(delta)) > e:
        x_copy = copy(x)
        for k in range(n):
            sum=0
            for j in range(n):
                if j!=k:
                    sum =sum + x[j]*a[k,j]
            x[k]=b[k]-sum
        print(x)
        delta = x_copy-x
        i+=1
        
   
    return x,i


def simple_iter(a,b):
    n = a.shape[0]
    e = 0.000001
    i = 0
    
    for k in range(n):
        b[k] = b[k]/a[k,k]
        a[k]=a[k]/a[k,k]

    x = zeros(n)
    x_prev = zeros(n)
    delta = ones(n)

    while max(abs(delta)) > e:
        for k in range(n):
            
            sum=0
            for j in range(n):
                if j!=k:
                    sum =sum + x_prev[j]*a[k,j]           
            x[k]=b[k]-sum
            
        print(x)
        delta = x_prev-x
        i+=1
        x_prev = copy(x)
   
    return x,i

'''
a_data=([[0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
        [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
        [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
        [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
        [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
        [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
        [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]])

b_data=([ 0.096,1.252,1.024,1.023,1.155,1.937,1.673])
'''
a_data=([[10,2,1,1],
        [1,10,2,1],
        [1,1,10,1],
        [3,0,4,20]])

b_data=([10,12,8,17])

A = array(a_data,float)
B = array(b_data,float)
set_printoptions(precision = 3)
print('Answer:',)
#print(simple_iter(A,B))
print(zeidal(A,B))
#print(relax(A,B))
#print('')