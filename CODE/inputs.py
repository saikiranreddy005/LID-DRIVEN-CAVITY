#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
def inputs():
    nx=4
    ny=4
    d_x=1/(nx-1)
    d_y=1/(ny-1)
    eta=d_x/d_y
    u_inf=1.0 ##top velocity
    mu=0.01
    v1=np.zeros([nx,ny])
    u1=np.zeros([nx,ny])
    si1=np.zeros([nx,ny])*0
    om1=np.zeros([len(u1),len(u1)])
    for j in range(len(u1)):
        om1[j,:]=0.5 #(2.0*u_inf/d_y)*((j/(nx-1)/len(u1))
    return mu,u_inf,eta,nx,ny,d_x,d_y,u1,v1,si1,om1

