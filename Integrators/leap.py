def method(q1,p1,dq,dp,t1,dt):
    a1=[0.5,0.5]
    b1=[0,1]
    A=[dq,dp]
    
    for i in range(len(a1)):
        q1+=b1[i]*dt*A[0](q1,p1,t1)
        p1+=a1[i]*dt*A[1](q1,p1,t1)
    t1+=dt
    return q1,p1,t1
