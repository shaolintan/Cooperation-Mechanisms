import consensus_evol as ce
import networkx as nx
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

g=nx.karate_club_graph()
N=g.order()
size=g.size()
deg=g.degree()
node_seq=sorted(deg.iteritems(),key=itemgetter(1),reverse=True)

gm=[[0.9,-0.1],[1,0]]

rslt=ce.interven_imi_evol_node_times(g,gm,0.1,140,5,0,node_seq[0][0],3)

np.save('boost_cooper_3.npy',rslt[2])

print rslt[1][419]/float(2*size)

#for d in g.nodes():
    #plt.plot(rslt[2][d])

#plt.xlabel("Iterations",fontsize=12,fontweight="heavy")
#plt.ylabel("Individuals' strategies",fontsize=12,fontweight="heavy")

#plt.show()
