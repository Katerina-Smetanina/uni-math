from numpy import *
from cmath import cos, pi
from numpy.linalg import solve
from numpy.linalg import eigh
from rotate import rotate

def norm(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])

def richardson(A, b):

    eps = 10**(-3)
    lambd = rotate(A, 4)
    print('lambda:', lambd)

    tau0 = 2/(max(lambd)+min(lambd))
    eta = min(lambd)/max(lambd)
    ro = (1-eta)/(1+eta)
  
    ro0 = (1 - sqrt(eta))/(1 + sqrt(eta))
    n = int(log(2/eps)/log(1/ro0))
    #n = 7
    #print('n = ', n)

    x = array(zeros(A.shape[0]), float)
    x = array([2, 2.5])
    x_new = array(ones(A.shape[0]), float)
    iterations = 0

    while norm(x, x_new) > eps:
        
        for k in range(1, n+1):
            x = copy(x_new)
            v = cos((2*k-1)*pi/(2*n))
            tau = tau0/(1+ro*v)
            x_new = ((b - dot(A,x))*tau + x).real
        
        iterations += n
        print(iterations)
    print(f'eps: {eps}')
    print(f'iterations: {iterations}')
    print(f'n: {n}')

    return x

A=([[2,1],
    [1,2]])


b = [4, 5]


set_printoptions(linewidth=1000)
#set_printoptions(precision=4,floatmode='fixed')

A = array(A, float)
b = array(b, float)
'''
print('A:')
print(A)
print('b: ', b)
'''
r = richardson(A, b)
print('solution: ', r)

print('Python solution: ', (solve(A, b)))
print()
print(abs(r-solve(A,b)))
