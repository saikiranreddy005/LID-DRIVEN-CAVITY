#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import LU


# In[1]:


def V(v,si,d_x):
    k=-len(v)
    v[0,:],v[-1,:],v[:,0],v[:,-1]=0,0,0,0
    for i in range(1,len(v)-1):
         for j in range(-2,k,-1):
                  v[j][i]=(-si[j][i+1]+si[j][i-1])/(2*d_x)
    return v

