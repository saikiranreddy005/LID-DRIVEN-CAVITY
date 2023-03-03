def U(u,si,d_y):
    k=-len(u)
    u[0,:],u[-1,:],u[:,0],u[:,-1]=1,0,0,0    
    for j in range(-2,k,-1):
        for i in range(1,len(u)-1):
                  u[j][i]=(si[j-1][i]-si[j+1][i])/(2*d_y)
    return u