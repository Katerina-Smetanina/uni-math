from numpy import *
from numpy.linalg import eigh
from sympy import python

def sign(x):
    if(x >= 0):
        return 1
    else:
        return -1


def condition(a,i,j):
    sigma = 1
    p = 4
    while abs(a[i,j]) < 10**-sigma:
            sigma += 1
    if sigma > p or a[i,j] == 0:
        return False
    else:
        return True

def rotate(a):
    n = a.shape[0]
    iteration = 0
    
    i = 0
    j = 1
    while condition(a, i, j) == True:
        C = array(zeros([n,n]))

        i = 0
        j = 1
        for g in range(n):
            for h in range(n):
                if g != h:
                    if abs(a[g,h]) > abs(a[i,j]):
                        i = g
                        j = h
                        
        d = sqrt((a[i,i] - a[j,j])**2 + 4*a[i,j]**2)
        s = sign(a[i,j]*(a[i,i] - a[j,j]))*sqrt((1 - abs(a[i,i]-a[j,j])/d)/2)
        c = sqrt((1 + abs(a[i,i]-a[j,j])/d)/2)                    
        
        for k in [w for w in range(0,min(i,j))]+[w for w in range(min(i,j)+1,max(i,j))]+[w for w in range(max(i,j)+1,n)]:
            for l in [w for w in range(0,min(i,j))]+[w for w in range(min(i,j)+1,max(i,j))]+[w for w in range(max(i,j)+1,n)]:
                C[k,l] = a[k,l]
        
        
        for k in range(n):
            if k!=i and k!=j:
                C[k,i] = c*a[k,i] + s*a[k,j]
                C[i,k] = C[k,i]
                C[k,j] = -s*a[k,i] + c*a[k,j]
                C[j,k] = C[k,j]
            
        C[i,i] = c**2 * a[i,i] + 2*c*s*a[i,j] + s**2 *a[j,j]
        C[j,j] = s**2 * a[i,i] - 2*c*s*a[i,j] + c**2 *a[j,j]
        
        iteration += 1
        a = C

    lambd = [a[i,i] for i in range(n)]
    
    return lambd

if __name__ == "__main__":
    a_data=([[1.0, 0.42, 0.54, 0.66],
             [0.42, 1.0, 0.32, 0.44],
             [0.54, 0.32, 1.0, 0.22],
             [0.66, 0.44, 0.22, 1.0]])


    set_printoptions(linewidth=1000)
    set_printoptions(precision=4,floatmode='fixed')

    A = array(a_data,float)
    lambd = rotate(A)

    print('solution:', lambd)

    pysolv = eigh(A)[0]
    print('python solution:', pysolv)

    lambd.sort()
    pysolv.sort()
    print('eps:', abs(lambd-pysolv))
