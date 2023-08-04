import math
from numpy import *
from numpy.linalg import solve
 
# Пробные данные для уравнения A*X = B
a = [[ 10.8000, 0.0475,      0, 0     ],
     [  0.0321, 9.9000, 0.0523, 0     ],
     [       0, 0.0369, 9.0000, 0.0570],
     [       0,      0, 0.0416, 8.1000]]
 
b = [12.1430, 13.0897, 13.6744, 13.8972]
 
# Решение, которое должно получиться:
# x1 = 1,118587
# x2 = 1,310623
# x3 = 1,503186
# x4 = 1,707983
  
# Проверка 3х-диаг. матрицы коэффициентов на корректность
def isCorrectArray(a):
    n = len(a)
    
    for row in range(0, n):
        if( len(a[row]) != n ):
            print('Не соответствует размерность')
            return False
        
    for row in range(1, n - 1):
        if(abs(a[row][row]) < abs(a[row][row - 1]) + abs(a[row][row + 1])):
            print('Не выполнены условия достаточности')
            return False
 
    if (abs(a[0][0]) < abs(a[0][1]))or(abs(a[n - 1][n - 1]) < abs(a[n - 1][n - 2])):
        print('Не выполнены условия достаточности')
        return False
        
    
    for row in range(0, len(a)):
        if( a[row][row] == 0 ):
            print('Нулевые элементы на главной диагонали')
            return False
    return True
 
 
def solution(a, b):
    if( not isCorrectArray(a) ):
        print('Ошибка в исходных данных')
        return -1 
 
    n = len(a)
    x = zeros(n) # обнуление вектора решений
    v = zeros(n)
    u = zeros(n)

    # для первой 0-й строки
    v[0] = a[0][1] / (-a[0][0]) 
    u[0] = ( - b[0]) / (-a[0][0])
    
    for i in range(1, n - 1):
        v[i] = a[i][i+1] / ( -a[i][i] - a[i][i-1]*v[i-1] )
        u[i] = ( a[i][i-1]*u[i-1] - b[i] ) / ( -a[i][i] - a[i][i-1]*v[i-1] )
        
    # для последней (n-1)-й строки
    v[n-1] = 0
    u[n-1] = (a[n-1][n-2]*u[n-2] - b[n-1]) / (-a[n-1][n-1] - a[n-1][n-2]*v[n-2])
    
#    print('Прогоночные коэф v: ', v)
 #   print('Прогоночные коэф u: ', u)
    
    # Обратный ход
    x[n-1] = u[n-1]
    for i in range(n-2, -1, -1):
        x[i] = v[i] * x[i+1] + u[i]    
    return x    
                
    
print('Решение: ','x', solution(a, b))
print('Погрешность',abs(solution(a,b)-solve(a,b)))