import consensus_evol as ce
import networkx as nx
import numpy as np

g=nx.karate_club_graph()
N=g.order()
size=g.size()
deg=[]
club1=[]
club2=[]
club3=[]
club4=[]
club5=[]
gm=[[0.9,-0.1],[1,0]]

for d in g.nodes():
    rslt1=ce.interven_imi_evol_node(g,gm,0,1000,0,0,d)
    rslt2=ce.interven_imi_evol_node(g,gm,0.1,1000,0,0,d)
    rslt3=ce.interven_imi_evol_node(g,gm,0.5,1000,0,0,d)
    rslt4=ce.interven_imi_evol_node(g,gm,0.1,1000,5,0,d)
    rslt5=ce.interven_imi_evol_node(g,gm,0.5,1000,5,0,d)
    deg.append(g.degree(d))
    club1.append(rslt1[1][999]/float(2*size))
    club2.append(rslt2[1][999]/float(2*size))
    club3.append(rslt3[1][999]/float(2*size))
    club4.append(rslt4[1][999]/float(2*size))
    club5.append(rslt5[1][999]/float(2*size))

np.save('club1.npy',club1)
np.save('club2.npy',club2)
np.save('club3.npy',club3)
np.save('club4.npy',club4)
np.save('club5.npy',club5)
np.save('deg.npy',deg)

    
