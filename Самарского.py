import math
from numpy import *
from numpy.linalg import solve

 
# Решение, которое должно получиться:
# x1 = 1,118587
# x2 = 1,310623
# x3 = 1,503186
# x4 = 1,707983
 
 
def solution(arr, b_arr):

    n = len(arr)
    x = zeros(n) 
    b = arr[0][0]
    a = arr[1][0]
    f = b_arr[0]
    ph = b_arr[1]
    l = zeros(n)
    l[0] = 1
    
    alpha = zeros(n)
    beta = zeros(n)
    m = zeros(n)
    # для первой 0-й строки

    
    for k in range(0, n - 2):
        if abs(b) >= abs(arr[k][k+1]):
            alpha[k]= (-arr[k][k+1])/b
            beta[k] = f/b
            
            b = arr[k+1][k+1] + alpha[k]*a
            f = ph - a*beta[k]
            m[k+1] = l[k]
            l[k+1] = k+1
            a = arr[k+2][k+1]
            ph = b_arr[k+2]
        else:
            alpha[k] = (-b)/arr[k][k+1]
            beta[k] = f / arr[k][k+1]
            
            b = a + alpha[k]*arr[k+1][k+1]
            f = ph-beta[k]*arr[k+1][k+1]
            m[k+1] = k+1
            l[k+1] = l[k]
            a = alpha[k]*arr[k+2][k+1]
            ph = b_arr[k+2] - beta[k]*arr[k+2][k+1]
            
    k = n-2
    if abs(b) >= abs(arr[k][k+1]):     
        alpha[k]= (-arr[k][k+1])/b
        beta[k] = f/b
        
        b = arr[k+1][k+1] + alpha[k]*a
        f = ph - a*beta[k]
        m[k+1] = l[k]
        l[k+1] = k+1

    else:
        alpha[k] = (-b)/arr[k][k+1]
        beta[k] = f / arr[k][k+1]
        
        b = a + alpha[k]*arr[k+1][k+1]
        f = ph-beta[k]*arr[k+1][k+1]
        m[k+1] = k+1
        l[k+1] = l[k]

    x[n-1] = f/b
    #вопросики с обратным ходом654
    for k in range(n-2, -1, -1):    
        x[k] = alpha[k]*x[k+1]+beta[k]
        
  #  print('Прогоночные коэф alpha: ', alpha)
   # print('Прогоночные коэф beta: ', beta)

    return x
a = ([0.1, 2, 0, 0],
[3, 0.4, 0.5, 0],
[0, 6, 7, -8],
[0, 0, 9, 1])

b = [1.5, 6.8, 7, 9]

print('Решение: ','x', solution(a, b))
sol = solution(a,b)
sol.sort()
print('Погрешность',abs(sol-solve(a,b)))