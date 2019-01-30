import numpy as np

#Runge-Kutta 4th Order

def method(q1,p1,dq,dp,t,dt):
    m=2 				# Number of differential equations
    k1=[0.0]*m 
    k2=[0.0]*m
    k3=[0.0]*m
    k4=[0.0]*m
        
    A=[dq,dp] 			#Name of the differential equations
    
    for s in range(len(A)):
        k1[s]=dt*(A[s](q1,p1,t))
    for s in range(len(A)):
         k2[s]=dt*A[s](q1+0.5*k1[0],p1+0.5*k1[1],t+(dt/2.0))
    for s in range(len(A)):
        k3[s]=dt*A[s](q1+0.5*k2[0],p1+0.5*k2[1],t+(dt/2.0))
    for s in range(len(A)):
        k4[s]=dt*A[s](q1+k3[0],p1+k3[1],t+h)
        
    q1+=(1./6.0)*(k1[0]+2.0*k2[0]+2.0*k3[0]+k4[0])
    p1+=(1./6.0)*(k1[1]+2.0*k2[1]+2.0*k3[1]+k4[1])
    t+=dt
    
    return q1,p1,t
