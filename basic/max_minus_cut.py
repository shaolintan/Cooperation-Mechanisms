import networkx as nx
from operator import itemgetter


def divide_sign_graph(g):
    g1=g.copy()
    g2=g.copy()
    for e in g1.edges_iter(data=True):
        if e[2]['weight']<0: g1.remove_edges_from([e])
    for e in g2.edges_iter(data=True):
        if e[2]['weight']>0: g2.remove_edges_from([e])
    return [g1,g2]

def dynamics1(g,comp):
    for node1 in comp:
        a=set(g.nodes())-set(comp)
        a=a.intersection(set(g.neighbors(node1)))
        for node2 in a:
            g[node1][node2]['weight']=-g[node1][node2]['weight']
    return g

def find_sign_number(g,comp):
    sign_number=0
    for node1 in comp:
        a=set(g.nodes())-set(comp)
        a=a.intersection(set(g.neighbors(node1)))                   
        for node2 in a:
            sign_number+=g[node1][node2]['weight']
    return sign_number

def sign_degree_sequence(g):
    degree=[]
    for node1 in g.nodes_iter():
        a=0
        for node2 in g.neighbors_iter(node1):
            a+=g[node1][node2]['weight']
        degree.append((node1,a))
    degree=sorted(degree,key=itemgetter(1))
    return degree


            


    


            
            
            
    

