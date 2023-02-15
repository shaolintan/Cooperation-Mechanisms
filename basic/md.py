import max_minus_cut as mmc
import networkx as nx
import dynamic as dn
import ban1

g=nx.Graph()
g.add_weighted_edges_from([(1,2,1),(1,3,1),(2,4,1),(3,4,1),(1,4,1),(3,5,1),(4,5,1),\
                           (1,6,1)])
ban_lev1=ban1.balance_level(g)

if nx.is_connected(g):
    while True:
       [g1,g2]=mmc.divide_sign_graph(g)
       if nx.is_connected(g1): break
       a=nx.connected_components(g1)
       g=mmc.dynamics1(g,a[0])


while True:
    degree=mmc.sign_degree_sequence(g)
    comp=degree[0][0]
    comp=dn.generate_comp3(g,comp)
    if set(g.nodes())==set(comp): break  
    g=mmc.dynamics1(g,comp)
ban_lev2=ban1.balance_level(g)

print ban_lev1,ban_lev2
