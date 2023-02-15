import consensus_evol as ce
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

g=nx.krackhardt_kite_graph()
N=g.order()

cen1=nx.degree_centrality(g)
cen2=nx.closeness_centrality(g)
cen3=nx.betweenness_centrality(g)
cen4=nx.eigenvector_centrality(g)


cen5={}
for d1 in g.nodes_iter():
    cen5[d1]=0
    for d2 in g.neighbors_iter(d1):
        cen5[d1]+=1/float(g.degree(d2))

node_seq1=sorted(cen1.iteritems(),key=itemgetter(1),reverse=True)
node1=node_seq1[0][0]
node_seq2=sorted(cen2.iteritems(),key=itemgetter(1),reverse=True)
node2=node_seq2[0][0]
node_seq3=sorted(cen3.iteritems(),key=itemgetter(1),reverse=True)
node3=node_seq3[0][0]
node_seq4=sorted(cen4.iteritems(),key=itemgetter(1),reverse=True)
node4=node_seq4[0][0]
node_seq5=sorted(cen5.iteritems(),key=itemgetter(1),reverse=True)
node5=node_seq5[0][0]
node_seq6=sorted(cen1.iteritems(),key=itemgetter(1))
node6=node_seq6[0][0]

print node1
print node2
print node3
print node4
print node5
print node6

gm=[[0.9,-0.1],[1,0]]
rslt1=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node1)
rslt2=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node2)
rslt3=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node3)
rslt4=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node4)
rslt5=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node5)
rslt6=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,node6)

plt.plot(rslt1[1],'ro')
plt.plot(rslt2[1],'bo')
plt.plot(rslt3[1],'mo')
plt.plot(rslt4[1],'co')
plt.plot(rslt5[1],'go')
plt.plot(rslt6[1],'ko')

plt.show()

