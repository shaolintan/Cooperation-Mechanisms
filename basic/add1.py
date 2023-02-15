import random
def add(g):
    a={}
    p={}
    for d in g.nodes_iter():
	    a[d]=random.choice([1,-1])
	    p[d]=0
    nx.set_node_attributes(g,'strategy',a)
    nx.set_node_attributes(g,'payoff',p)
    return [g,a,p]

import networkx as nx
g1=nx.Graph()
g1.add_nodes_from([1,2,4])
[g2,c,e]=add(g1)
print c
print e
a=g1.nodes()
b=g2.node[2]['strategy']
print a
print b
