import networkx as nx
import random

class multiagent_dynamics:

    def add_dynamic_attributes(self,g):
        a=p={}
        for d in g.nodes_iter():
            a[d]=random.choice([1,-1])
            p[d]=0
        nx.set_node_attributes(g,'strategy',a)
        nx.set_node_attributes(g,'payoff',p)
        return g

    def add_dynamic_edge_attribute(self,g):
        b={}
        for e in g.edges_iter(g):
            b[e]=random.choice([1,-1])
        nx.set_edge_attributes(g,'weight',b)
        return g

    def update_payoff(self,g):
        for d1 in g.nodes_iter():
            mid_var=0
            for d2 in g.neighbors_iter(d1):
                mid_var+=g.node[d1]['strategy']*g.node[d2]['strategy']*g[d1][d2]['weight']
            g.node[d1]['payoff']=mid_var
        return g

    def update_strategy(self,g):
        uphappen=0
        for d1 in g.nodes_iter():
            if g.node[d1]['payoff']<0 or (g.node[d1]['payoff']==0 and random.random()>=0.5):
                g.node[d1]['strategy']=-g.node[d1]['strategy']
                uphappen=1
        return [g,uphappen]

   
          
    

            
    
            
    
    
    
