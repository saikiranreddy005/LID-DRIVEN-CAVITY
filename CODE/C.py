#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import LU


# In[3]:


def SI(si,eta,d_x,om):
    k=-len(si)
    si[0][0],si[0][-1],si[-1][0],si[-1][-1]=0,0,0,0
    si0=si    
    for j in range(-2,k,-1):
            A=np.zeros([-k-2,-k])
            B=np.zeros(-k-2)
            for i in range(1,len(si)-1):
                    A[i-1][i]=2*(1+eta**2)
                    A[i-1][i+1]=-1
                    A[i-1][i-1]=-1
                    B[i-1]=eta**2*(si[j-1][i]+si[j+1][i])+d_x**2*om[j][i]
            B=B-A[:,0]*si[j][0]-A[:,-1]*si[j][-1]
            si[j,1:-1]=LU.solve(A[:,1:-1],B)
            #print(si)
    for i in range(1,len(si)-1):
            A=np.zeros([-k-2,-k])
            B=np.zeros(-k-2)
            for j in range(1,-k-1):
                    A[j-1][j]=2*(1+eta**2)
                    A[j-1][j+1]=-eta**2
                    A[j-1][j-1]=-eta**2
                    B[j-1]=(si[-j-1][i+1]+si[-j-1][i-1])+(d_x**2*om[-j-1][i])
            B=B-A[:,0]*si[-1][i]-A[:,-1]*si[0][i]
            si[-2:k:-1,i]=LU.solve(A[:,1:-1],B)
    err=sum(sum(abs(si0-si)))
    if err<pow(10,-4):
            flag=False
    return si 

