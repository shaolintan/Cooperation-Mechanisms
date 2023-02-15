import numpy as np
import networkx as nx

from operator import itemgetter

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


# the one step updating in continuous imitation dynamics
def obtain_fitness(G,gm):
    f={}
    for d1 in G.nodes_iter():
        f[d1]=0
        for d2 in G.neighbors_iter(d1):
            f[d1]=f[d1]+np.dot(np.dot([G.node[d1]['prob'],1-G.node[d1]['prob']],gm),
                             [G.node[d2]['prob'],1-G.node[d2]['prob']])
    nx.set_node_attributes(G,'fitness',f)
    return G

def imi_one_step_evol(G,w):
    det={}
    f=nx.get_node_attributes(G,'fitness')
    for d1 in G.nodes_iter():
        det[d1]=0
        for d2 in G.neighbors_iter(d1):
            det[d1]=det[d1]+(np.tanh(w*(f[d2]-f[d1]))+1)*(G.node[d2]['prob']-G.node[d1]['prob'])/float(2*G.degree(d1))
    for d1 in G.nodes_iter():
        G.node[d1]['prob']+=det[d1]
    return G

def imi_evol(G,gm,dis,w,M):
    G=add_dynamic_attributes(G,dis)
    seq=[]
    seq2={}
    size=G.size()
    order=G.order()
    seq3=[]
    for d in G.nodes_iter():
        seq2[d]=[]
    for i in range(M):
        s=0
        mid=[]
        for d in G.nodes_iter():
            seq2[d].append(G.node[d]['prob'])
            s+=G.node[d]['prob']*G.degree(d)
            mid.append(G.node[d]['prob'])
        mid=np.sort(mid)
        mid2=abs(mid[0]-mid[order-1])
        seq3.append(mid2)
        seq.append(s/float(size)/2)
        G=obtain_fitness(G,gm)
        G=imi_one_step_evol(G,w)
    return (G,seq,seq2,seq3)

# intervention of the imitation dynamics
def award_the_best(G,u):
    p=nx.get_node_attributes(G,'prob')
    p_1=sorted(p.iteritems(),key=itemgetter(1),reverse=True)
    G.node[p_1[0][0]]['fitness']+=u
    return G

def interven_imi_evol_1(G,gm,dis,w,M,u):
    G=add_dynamic_attributes(G,dis)
    seq=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
        seq.append(s)
        G=obtain_fitness(G,gm)
        G=award_the_best(G,u)
        G=imi_one_step_evol(G,w)
    return (G,seq)

def punish_the_worst(G,u):
    p=nx.get_node_attributes(G,'prob')
    p_1=sorted(p.iteritems(),key=itemgetter(1))
    G.node[p_1[0][0]]['fitness']-=u
    return G

def interven_imi_evol_2(G,gm,dis,w,M,u):
    G=add_dynamic_attributes(G,dis)
    seq=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
        seq.append(s)
        G=obtain_fitness(G,gm)
        G=punish_the_worst(G,u)
        G=imi_one_step_evol(G,w)
    return (G,seq)

def proportional_award(G,u):
    p=nx.get_node_attributes(G,'prob')
    s=0
    for d in G.nodes_iter():
        s+=p[d]
    for d in G.nodes_iter():
        G.node[d]['fitness']+=p[d]/float(s)*u
    return G
    
def interven_imi_evol_3(G,gm,dis,w,M,u):
    G=add_dynamic_attributes(G,dis)
    seq=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
        seq.append(s)
        G=obtain_fitness(G,gm)
        G=proportional_award(G,u)
        G=imi_one_step_evol(G,w)
    return (G,seq)

def interven_imi_evol_1(G,gm,dis,w,M,u):
    G=add_dynamic_attributes(G,dis)
    seq=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
        seq.append(s)
        G=obtain_fitness(G,gm)
        G=award_the_best(G,u)
        G=imi_one_step_evol(G,w)
    return (G,seq)
    

# intervention of the cooperation level through intervention the strategy of one node
def interven_imi_evol_node(G,gm,w,M,u,p,d):
    N=G.order()
    value=p*np.ones(N)
    G=add_dynamic_attributes(G,value)
    G.node[d]['prob']=1
    G=obtain_fitness(G,gm)
    G.node[d]['fitness']+=u
    seq1=[]
    seq2={}
    for d in G.nodes():
        seq2[d]=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
            seq2[d].append(G.node[d]['prob'])
        seq1.append(s)
        G=imi_one_step_evol(G,w)
        G=obtain_fitness(G,gm)
    return (G,seq1,seq2)



# intervention of the cooperation level through intervention the strategy of several nodes
def interven_imi_evol_nodes(G,gm,w,M,u,p,bench):
    N=G.order()
    value=p*np.ones(N)
    G=add_dynamic_attributes(G,value)
    for d in bench:
        G.node[d]['prob']=1
    G=obtain_fitness(G,gm)
    for d in bench:
        G.node[d]['fitness']+=u
    seq1=[]
    seq2={}
    for d in G.nodes():
        seq2[d]=[]
    for i in range(M):
        s=0
        for d in G.nodes_iter():
            s+=G.node[d]['prob']*G.degree(d)
            seq2[d].append(G.node[d]['prob'])
        seq1.append(s)
        G=imi_one_step_evol(G,w)
        G=obtain_fitness(G,gm)
    return (G,seq1,seq2)

# intervention of the cooperation level through intervention the strategy of one node for several times
def interven_imi_evol_node_times(G,gm,w,M,u,p,d,times):
    N=G.order()
    value=p*np.ones(N)
    G=add_dynamic_attributes(G,value)
    G.node[d]['prob']=1
    G=obtain_fitness(G,gm)
    G.node[d]['fitness']+=u
    seq1=[]
    seq2={}
    for d in G.nodes():
        seq2[d]=[]
    for k in range(times):
        for i in range(M):
            s=0
            for d in G.nodes_iter():
                s+=G.node[d]['prob']*G.degree(d)
                seq2[d].append(G.node[d]['prob'])
            seq1.append(s)
            G=imi_one_step_evol(G,w)
            G=obtain_fitness(G,gm)
        G.node[d]['prob']=1
        G=obtain_fitness(G,gm)
        G.node[d]['fitness']+=u
    return (G,seq1,seq2)
    
            
    
    
    
