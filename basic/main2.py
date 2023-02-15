import max_minus_cut as mmc
import networkx as nx
import dynamic as dn
import ban1
import multiagent_dynamics2 as md


g=nx.Graph()
g=nx.read_weighted_edgelist('C:\Documents and Settings\hp\My Documents\Downloads\data\EGFR_symm.txt')
ban_lev1=ban1.balance_level(g)


if nx.is_connected(g):
    while True:
       [g1,g2]=mmc.divide_sign_graph(g)
       if nx.is_connected(g1): break
       a=nx.connected_components(g1)
       g=mmc.dynamics1(g,a[0])


comp=[]
while True:
    comp=dn.generate_comp1(g,comp)
    g=mmc.dynamics1(g,comp)
    if set(g.nodes())==set(comp):
        break
    
ban_lev2=ban1.balance_level(g)

print ban_lev1,ban_lev2



    

