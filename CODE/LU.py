


import numpy as np
def solve(a,b):
    n=len(a)
    for k in range(n-1):
        for i in range(k+1,n):
            if a[i,k]!=0.0:
                lam=a[i,k]/a[k,k]
                a[i,k+1:n]=a[i,k+1:n]-lam*a[k,k+1:n]
                a[i,k]=lam
    for k in range(1,n):
        b[k]=b[k]-np.dot(a[k,0:k],b[0:k])
    b[n-1]=b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
         b[k]=(b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

a=np.array([[1.0,4.0,1.0],[1.0,6.0,-1.0],[2.0,-1.0,2.0]])
b=np.array([7.0,13.0,5.0])
print(solve(a,b))




# In[ ]:




