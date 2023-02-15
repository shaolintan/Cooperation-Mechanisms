import networkx as nx
import random


def add_dynamic_attributes(g):
    a={}
    p={}
    for d in g.nodes_iter():
        a[d]=1
        p[d]=0
    nx.set_node_attributes(g,'strategy',a)
    nx.set_node_attributes(g,'payoff',p)
    return g

def add_dynamic_edge_attribute(g):
    b={}
    for e in g.edges_iter(g):
        b[e]=-1
    nx.set_edge_attributes(g,'weight',b)
    return g

def update_payoff(g):
    total_payoff=0
    for d1 in g.nodes_iter():
        mid_var=0
        for d2 in g.neighbors_iter(d1):
            mid_var=mid_var+g.node[d1]['strategy']*g.node[d2]['strategy']*g[d1][d2]['weight']
        g.node[d1]['payoff']=mid_var
        total_payoff+=mid_var
    return [g,total_payoff]

def update_strategy1(g):
    uphappen=0
    for d1 in g.nodes_iter():
        if g.node[d1]['payoff']<0:
            g.node[d1]['strategy']=-g.node[d1]['strategy']
            uphappen=1
    return [g,uphappen]

def update_strategy2(g):
    uphappen=0
    for d1 in g.nodes_iter():
       if g.node[d1]['payoff']<0 or (g.node[d1]['payoff']==0 and random.random()>=0.5):
           g.node[d1]['strategy']=-g.node[d1]['strategy']
           uphappen=1
           break
    return [g,uphappen]

