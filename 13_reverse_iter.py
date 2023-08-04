import math
from numpy import *
from numpy.linalg import norm, eigh
from qr import QR

def max_abs(x):
    return max([abs(i) for i in x])

def revers_iter(a):
    eps = 10**(-3)
    i = 0
    delta = 1
    n = a.shape[0]
    x_prev = ones(n)
    x = QR(a, x_prev/max_abs(x_prev))
    
    while abs(delta) > eps:
        i += 1
        x_prev = copy(x)
        x = QR(a, x_prev/max_abs(x_prev))
        delta = 1/max_abs(x) - 1/max_abs(x_prev)
    
    return 1/max_abs(x), x, i

a_data =([[2.2, 1, 0.5,2],
        [1, 1.3, 2, 1],
        [0.5, 2, 0.5, 1.6],
        [2, 1, 1.6, 2]])

A = array(a_data,float)

set_printoptions(precision = 3)
print('Answer:',)
print(revers_iter(A))

lambd, x, k = revers_iter(A)
print(f'lambda: {lambd}')
print(f'x: {x}')
print(f'iterations: {k}')

pysolv = eigh(A)[0]
print(f'python solution: {pysolv}')

