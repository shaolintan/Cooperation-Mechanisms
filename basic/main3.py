import max_minus_cut as mmc
import networkx as nx
import dynamic as dn
import ban1
import multiagent_dynamics2 as md


g=nx.Graph()
g=nx.read_weighted_edgelist('C:\Documents and Settings\hp\My Documents\Downloads\data\EGFR_symm.txt')
ban_lev1=ban1.balance_level(g)
print ban_lev1

graphCom=nx.connected_component_subgraphs(g)

for i in range(len(graphCom)):
    while True:
        [g1,g2]=mmc.divide_sign_graph(graphCom[i])
        if nx.is_connected(g1): break
        a=nx.connected_components(g1)
        graphCom[i]=mmc.dynamics1(graphCom,a[0])
    while True:
        degree=mmc.sign_degree_sequence(graphCom[i])
        comp=degree[0][0]
        comp=dn.generate_comp3(graphCom[i],comp)
        if set(graphCom[i].nodes())==set(comp): break  
        graphCom[i]=mmc.dynamics1(graphCom[i],comp)

ban_level=0
for i in range(len(graphCom)):
    ban_level+=ban1.balance_level(graphCom[i])
print ban_level

T=1000
for i in range(len(graphCom)):
     for j in range(T):
        degree=mmc.sign_degree_sequence(graphCom[i])
        comp=degree[0][0]
        comp=dn.generate_comp1(graphCom[i],comp)
        if set(graphCom[i].nodes())==set(comp): break  
        graphCom[i]=mmc.dynamics1(graphCom[i],comp)
        j+=1

ban_lev2=0
for i in range(len(graphCom)):
    ban_lev2+=ban1.balance_level(graphCom[i])
print ban_lev2
    


    
    




