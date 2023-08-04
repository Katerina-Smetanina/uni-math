import math
import copy
from numpy import *
from numpy import linalg as LA

def A_U_Q(a,q,n,k):
    x = zeros([n,n])
    a_n= zeros([n,n])
    q_n = zeros([n,n])
    a_n[:k,0]=a[:k,0]
    q_n[0,:k]=q[:k]
    x = a_n.dot(q_n)
    return x

def ok(a,b):
    n = a.shape[0]
    V = zeros(a.shape[0])
    U = zeros([a.shape[0],1])
    V_A = zeros(a.shape[0])
    A_U = zeros([a.shape[0],1])
    a_minor = zeros([n,n], dtype = float)
    B = zeros([n-1,n-1])
    r = zeros(a.shape[0])
    a_kk = 0
    
    a_minor[0,0] = 1/a[0,0]
    for k in range(1,n):

        V[:k]=a[k,:k]
        U[:k,0]=a[:k,k]
        a_kk = a[k,k]
        V_A = V.dot(a_minor)
        A_U = a_minor.dot(U)
        alpha = 1/(a_kk-V.dot(A_U))
        
        r = -alpha * A_U
        q = -alpha * V_A
        B = a_minor - (A_U_Q(A_U,q,n,k))

        a_minor = B
        a_minor[k,:k] = q[:k]       
        a_minor[:k,k] = r[:k,0]
        a_minor[k,k]= alpha
    print('inver')
    print(a_minor)
    print('Answer')
    return a_minor

if __name__ == "__main__": 
    a_data=([[0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
            [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
            [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
            [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
            [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
            [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
            [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]])

    b_data=([ 0.096,1.252,1.024,1.023,1.155,1.937,1.673])

    A = array(a_data,float)
    B = array(b_data,float)
    set_printoptions(precision = 3)
    print('Answer:',)
    print(ok(A,B))
    print('Проверка')
    print(LA.inv(A) - ok(A,B) )
