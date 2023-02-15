import numpy as np
import random

def random_bool(N):
    a=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            a[i][j]=random.choice([0,1])
    return a



def produc(g1,g2):
    s=g1.shape
    b=np.zeros(s)
    for i in range(s[1]):
        for j in range(s[1]):
            for k in range(s[1]):
                b[i][j]=(b[i][j] or (g1[i][k] and g2[k][j]))                 
    return b

def multi_produc(g1,k):
    r=[]
    r.append(produc(g1,g1))
    for i in range(1,k):
        a=produc(g1,r[i-1])
        r.append(a)
    return r


        
        
                         
                         
                
            
