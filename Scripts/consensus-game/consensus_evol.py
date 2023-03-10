import numpy as np
import networkx as nx

# initiate the nodes with given value
def add_dynamic_attributes(g,value):
    a={}
    i=0
    for d1 in g.nodes():
        a[d1]=value[i]
        i=i+1
    nx.set_node_attributes(g,'prob',a)        
    return g

def one_step_evol(G,gm):
    f={}
    for d1 in G.nodes_iter():
        f[d1]=0
        for d2 in G.neighbors_iter(d1):
            f[d1]=f[d1]+np.dot(np.dot([G.node[d1]['prob'],1-G.node[d1]['prob']],gm),
                             [G.node[d2]['prob'],1-G.node[d2]['prob']])
    s={}
    for d1 in G.nodes_iter():
        s[d1]=f[d1]
        for d2 in G.neighbors_iter(d1):
            s[d1]+=f[d2]
    for d1 in G.nodes_iter():
        for d2 in G.neighbors_iter(d1):
            G.node[d1]['prob']=G.node[d1]['prob']+f[d2]/float(s[d1])*(G.node[d2]['prob']
                            -G.node[d1]['prob'])
    return G

def evol(G,gm,dis,M):
    G=add_dynamic_attributes(G,dis)
    seq={}
    for d in G.nodes_iter():
        seq[d]=[]
    for i in range(M):
        for d in G.nodes_iter():
            seq[d].append(G.node[d]['prob'])
        G=one_step_evol(G,gm)
    return (G,seq)

def DB_one_step_evol(G,gm,w):
    f={}
    for d1 in G.nodes_iter():
        f[d1]=0
        for d2 in G.neighbors_iter(d1):
            f[d1]=f[d1]+np.dot(np.dot([G.node[d1]['prob'],1-G.node[d1]['prob']],gm),
                             [G.node[d2]['prob'],1-G.node[d2]['prob']])
        f[d1]=1-w+w*f[d1]
    s={}
    for d1 in G.nodes_iter():
        s[d1]=0
        for d2 in G.neighbors_iter(d1):
            s[d1]+=f[d2]
    m={}
    for d1 in G.nodes_iter():
        m[d1]=0
        for d2 in G.neighbors_iter(d1):
            m[d1]=m[d1]+f[d2]/float(s[d1])*G.node[d2]['prob']
    for d1 in G.nodes_iter():
        G.node[d1]['prob']=m[d1]
    return G

def DB_evol(G,gm,w,dis,M):
    G=add_dynamic_attributes(G,dis)
    seq={}
    for d in G.nodes_iter():
        seq[d]=[G.node[d]['prob']]
    for i in range(M):
        G=DB_one_step_evol(G,gm,w)
        for d in G.nodes_iter():
            seq[d].append(G.node[d]['prob'])
    return (G,seq)





    
    
                                                        
            
    
    
    
