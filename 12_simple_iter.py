import math
from numpy import *
from numpy.linalg import norm, eigh

def module(x):
    return sqrt(sum(x[i]**2 for i in range(len(x))))

def sign(x):
    if(x > 0):
        return 1
    else:
        return -1

def simple_iter(a):
    eps = 10**(-3)
    n = a.shape[0]
    i = 0
    lamda=0
    
    delta = ones(n)
    x = ones(n)
    x_prev = zeros(n)
    y = zeros(n)
    
    while max(abs(delta)) > eps:    
        x_prev = copy(x)
        y = a.dot(x)
        lamda = y.dot(x)
        x = y / module(y)
        
        i += 1
        delta = (sign(lamda) * x)- x_prev

    return lamda, x, i



a_data =([[2.2, 1, 0.5,2],
        [1, 1.3, 2, 1],
        [0.5, 2, 0.5, 1.6],
        [2, 1, 1.6, 2]])


A = array(a_data,float)

set_printoptions(precision = 3)
print('Answer:',)

lambd, x, i = simple_iter(A)
print(f'lambda: {lambd}')
print(f'x: {x}')
print(f'iterations: {i}')

