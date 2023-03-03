#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import LU


# In[ ]:


def OM(om,u,v,eta,d_x,d_y,mu,si,u_inf):
    k=-len(om)
    om[:,0]=-2*si[:,1]/d_x**2
    om[:,-1]=-2*si[:,-2]/d_x**2
    om[-1,:]=-2*si[-2,:]/d_y**2
    om[0,:]=-(2*u_inf*d_y+2*si[1,:])/d_y**2
    om[0][0],om[0][-1],om[-1][0],om[-1][-1]=0,0,0,0
    for j in range(-2,k,-1):
            A=np.zeros([-k-2,-k])
            B=np.zeros(-k-2)
            for i in range(1,len(si)-1):
                    A[i-1][i]=4
                    A[i-1][i+1]=-(1-(d_x*u[j][i]/(2*mu)))
                    A[i-1][i-1]=-(1+(d_x*u[j][i]/(2*mu)))
                    B[i-1]=(1+(d_y*v[j][i]/(2*mu)))*om[j+1][i]+(1-(d_y*v[j][i]/(2*mu)))*om[j-1][i]
            B=B-A[:,0]*om[j][0]-A[:,-1]*om[j][-1]
            om[j,1:-1]=LU.solve(A[:,1:-1],B)
           
    for i in range(1,len(si)-1):
            A=np.zeros([-k-2,-k])
            B=np.zeros(-k-2)
            for j in range(1,-k-1):
                    A[j-1][j]=2*(1+eta**2)
                    A[j-1][j+1]=-(1-(d_y*v[j][i]/(2*mu)))
                    A[j-1][j-1]=-(1+(d_y*v[j][i]/(2*mu)))
                    B[j-1]=(1-(d_x*u[-j-1][i]/(2*mu)))*om[-j-1][i+1]+(1+(d_x*u[-j-1][i]/(2*mu)))*om[-j-1][i-1]
            B=B-A[:,0]*om[-1][i]-A[:,-1]*om[0][i]
            om[-2:k:-1,i]=LU.solve(A[:,1:-1],B)       
    return om

