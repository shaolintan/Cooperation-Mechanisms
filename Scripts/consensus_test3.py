import consensus_evol as ce
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

gm=[[0.9,-0.1],[1,0]]
test=0

while test==0:
    g=nx.newman_watts_strogatz_graph(100,3,0.1)
    N=g.order()
    dis=np.random.rand(N)
    a=sum(dis)/N
    rslt=ce.imi_evol(g,gm,dis,0.5,1400)
    b=a*np.ones(1400)
    if rslt[1][99]>a:
        test=1
        for d in g.nodes():
            plt.plot(rslt[2][d])
        plt.plot(b,'k-.',linewidth=2)
        plt.xlabel('iterations',fontweight="heavy",fontsize=12)
        plt.ylabel('strategy',fontweight="heavy",fontsize=12)
        plt.show()



#plt.plot(rslt[3],'b^-')
#plt.plot(rslt[1],'rs-')
