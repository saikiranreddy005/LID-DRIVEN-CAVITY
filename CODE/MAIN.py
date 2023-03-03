
import matplotlib.pyplot as plt
import numpy as np
import LU
import inputs
import A,B,C,D
import pandas as pd
# import reload

def main():
       mu,u_inf,eta,n_x,n_y,d_x,d_y,u1,v1,si1,om1=inputs.inputs() 
       flag=True
       i=0
       while flag:
            u=A.U(u1,si1,d_y)
            v=B.V(v1,si1,d_x)
            si=C.SI(si1,eta,d_x,om1) 
            om=D.OM(om1,u,v,eta,d_x,d_y,mu,si,u_inf)
            u1=0.8*u+0.2*u1
            v1=0.8*v+0.2*v1
            si1=0.8*si+0.2*si1
            om1=0.8*om+0.2*om1        
            i=i+1
            if n_x<13 and i>11:
                    flag=False
            else:
                if i>181:
                    flag=False

       print(u.shape,n_x,n_y)
       ################################# (u_contour)
       x,y=np.linspace(0,1,n_x),np.linspace(0,1,n_y)
       x,y=np.meshgrid(x,y)
       fig,ax = plt.subplots()
       contourf_ = ax.contourf(x,y,u[-1::-1],cmap='inferno')
       cbar = fig.colorbar(contourf_)
       plt.xlabel('X')
       plt.ylabel('Y')  
       plt.title("u_velocity contour for {}".format([n_x,n_y]))
       plt.show()
       ##############################(v_ontour)
       fig,ax = plt.subplots()
       contourf_ = ax.contourf(x,y,v[-1::-1],cmap='inferno')
       cbar = fig.colorbar(contourf_)
       plt.xlabel('X')
       plt.ylabel('Y') 
       plt.title("V velocity contour for {}".format([n_x,n_y])) 
       plt.show()
       ######################################(stream_func_contour)
       fig,ax = plt.subplots()
       contourf_ = ax.contourf(x,y,si[-1::-1],cmap='inferno')
       cbar = fig.colorbar(contourf_)
       plt.xlabel('X')
       plt.ylabel('Y')  
       plt.title("SI contour for {}".format([n_x,n_y])) 
       plt.show()
       #############################################
       fig,ax = plt.subplots()
       contourf_ = ax.contourf(x,y,om[-1::-1],cmap='inferno')
       plt.xlabel('X')
       plt.ylabel('Y')  
       cbar = fig.colorbar(contourf_)
       plt.title("omega contour for {}".format([n_x,n_y])) 
       plt.show() 
       ###############################################
       fig,ax = plt.subplots()
       ax.plot(np.linspace(0,1,n_x),v[int((n_y-1)/2)-1])
       plt.ylabel('v')
       plt.xlabel('x_distance')
       plt.title('v_velocity along horizontal centreline') 
       plt.show() 
      ####################################
       fig,ax = plt.subplots()
       ax.plot(u[-1::-1][:,int((n_x-1)/2)-1],np.linspace(0,1,n_x))
       plt.xlabel('u')
       plt.ylabel('y_distance')
       plt.title('U_velocity along vertical centreline')
       plt.show()
       #pd.DataFrame.to_csv(pd.DataFrame(u),'U_{}'.format([n_x,n_y]))
       #pd.DataFrame.to_csv(pd.DataFrame(v),'V_{}'.format([n_x,n_y]))
       #pd.DataFrame.to_csv(pd.DataFrame(om),'omega_{}'.format([n_x,n_y]))
       #pd.DataFrame.to_csv(pd.DataFrame(si),'strfunc_{}'.format([n_x,n_y]))


# In[3]:


main()


# In[ ]:




