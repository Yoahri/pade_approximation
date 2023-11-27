import numpy as np
import math
import sympy as smp
from eliminacao_de_gauss import eliminacao_de_gauss

def pade_approximation(m,n,func):
    x=smp.symbols("x", real=True)
    func=func
    N=m+n
    a=[]
    for i in range(N+1):
        derivative=smp.diff(func,x,i)
        c=derivative.subs([(x,0)]).evalf()
        coef=c/math.factorial(i)
        a.append(coef)

    B=np.zeros((N+1,N+2))
    Q=np.zeros(m+1)
    P=np.zeros(n+1)

    Q[0]=1
    P[0]=a[0]

    for i in range(1,N+1):
        for j in range(1,i):
            if j<= n:
                B[i][j]=0
        if i <= n:
            B[i][i]=1
        for j in range(i+1,N+1):
            B[i][j]=0
        for j in range(1,i+1):
            if j <= m:
                B[i][n+j]= -a[i-j]
        for j in range(n+1+i,N+1):
            B[i][j]=0
        B[i][N+1]=a[i]
    B=B[1:,1:]
    solucao=eliminacao_de_gauss(B)
    for i in range(0,n):
        P[i+1]=solucao[i]
    index=1
    upper = 0
    lower = 0
    for i in range(n,len(solucao)):
        Q[index]=solucao[i]
        index+=1
    for i in range(0,len(P)):
        p=P[i]*(x**i)
        upper += p
    for i in range(0,len(Q)):
        q=Q[i]*(x**i)
        lower += q
    
    return (upper/lower)