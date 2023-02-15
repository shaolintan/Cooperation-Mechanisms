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
bench=[node_seq[0][0],node_seq[1][0],node_seq[2][0]]

gm=[[0.9,-0.1],[1,0]]

rslt=ce.interven_imi_evol_nodes(g,gm,0.1,140,5,0,bench)

np.save('boost_cooper_2.npy',rslt[2])

print rslt[1][139]/float(2*size)

#for d in g.nodes():
    #plt.plot(rslt[2][d])

#plt.xlabel("Iterations",fontsize=12,fontweight="heavy")
#plt.ylabel("Individuals' strategies",fontsize=12,fontweight="heavy")

#plt.show()
