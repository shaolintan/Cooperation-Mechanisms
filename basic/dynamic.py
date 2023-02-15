import networkx as nx
import max_minus_cut as mmc
from operator import itemgetter
import random

def generate_comp1(g,comp=[]):
    comp=[comp]
    while True:
        a=mmc.find_sign_number(g,comp)
        c=set(g.nodes())-set(comp)
        if a<0 or c==set(): break
        if a==0 and random.random()>0.8: break
        b=[]
        for d1 in c:
            d=mmc.find_sign_number(g,comp+[d1])
            b.append((d1,d))
        f=min(b,key=itemgetter(1))
        comp=comp+[f[0]]
    return comp


def generate_comp2(g):
    sign_degree=mmc.sign_degree_sequence(g)
    comp=[]
    for i in range(len(sign_degree)):
        a=mmc.find_sign_number(g,comp)
        if a<0: break
        comp=comp+[sign_degree[i][0]]
    return comp


def generate_comp3(g,comp):
    [g1,g2]=mmc.divide_sign_graph(g)
    comp_neighbors=g1.neighbors(comp)
    comp=[comp]
    while True:
        a=mmc.find_sign_number(g,comp)
        c=set(g.nodes())-set(comp)
        if a<0 or (not c): break
        b=[]
        for d1 in comp_neighbors:
            a=mmc.find_sign_number(g,comp+[d1])
            b.append((d1,a))
        f=min(b, key=itemgetter(1))
        comp=comp+[f[0]]
        comp_neighbors=(set(comp_neighbors)|set(g1.neighbors(f[0])))-set(comp)
    return comp

def zero_turn(g):
    sign_degree=mmc.sign_degree_sequence(g)
    turn_set=[]
    turn_set_neigbors=set([])
    for i in range(sign_degree):
        if sign_degree[i][1]>0: break
        if sign_degree[i][0] not in turn_set_neighbors:
            turn_set.append(sign_degree[i][0])
            turn_set_neighbors=turn_set_neighbors|g.neighbors(sign_degree[i][0])
    return trun_set

    
        
    
