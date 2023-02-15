import max_minus_cut as mmc
import networkx as nx
import dynamic as dn
import ban1
import multiagent_dynamics2 as md

g=nx.Graph()
g=nx.erdos_renyi_graph(15,0.2)
g=md.add_dynamic_edge_attribute(g)
ban_lev1=ban1.balance_level(g)
print ban_lev1

if nx.is_connected(g):
    while True:
       [g1,g2]=mmc.divide_sign_graph(g)
       if nx.is_connected(g1): break
       a=nx.connected_components(g1)
       g=mmc.dynamics1(g,a[0])
       ban_lev3=ban1.balance_level(g)
       print ban_lev3
    while True:
       degree=mmc.sign_degree_sequence(g)
       comp=degree[0][0]
       comp=dn.generate_comp3(g,comp)
       print comp
       if set(g.nodes())==set(comp): break  
       g=mmc.dynamics1(g,comp)
       ban_lev2=ban1.balance_level(g)
       print ban_lev2
else: print " the graph is not connceted"
    
