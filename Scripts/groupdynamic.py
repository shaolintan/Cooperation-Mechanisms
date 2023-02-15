import numpy as np
import random as rd
import evolDynamic as ed
import math
import networkx as nx

# calculate the accumerate fitness of each individual
def group_calculate_fitness(g,pm,w):
    zeros={}
    ones={}
    for d1 in g.nodes_iter():
        zeros[d1]=0
        ones[d1]=0
        zeros[d1]=zeros[d1]+1-g.node[d1]['type']
        ones[d1]=ones[d1]+g.node[d1]['type']
        for d2 in g.neighbors_iter(d1):
            zeros[d1]=zeros[d1]+1-g.node[d2]['type']
            ones[d1]=ones[d1]+g.node[d2]['type']
    payoff={}
    for d in g.nodes_iter():
        payoff[d]=0
    for d1 in g.nodes_iter():
        payoff[d1]=payoff[d1]+(g.node[d1]['type']*(pm[0][0]*ones[d1]+\
                   pm[0][1]*zeros[d1])+(1-g.node[d1]['type'])*(pm[1][0]*ones[d1]+\
                   pm[1][1]*zeros[d1]))/float(ones[d1]+zeros[d1])
        for d2 in g.neighbors_iter(d1):
            payoff[d2]=payoff[d2]+(g.node[d2]['type']*(pm[0][0]*ones[d1]+\
                   pm[0][1]*zeros[d1])+(1-g.node[d2]['type'])*(pm[1][0]*ones[d1]+\
                   pm[1][1]*zeros[d1]))/float(ones[d1]+zeros[d1])
    for d in g.nodes_iter():
        payoff[d]=math.exp(w*payoff[d])
    nx.set_node_attributes(g,'fitness',payoff)
    return g

# calculate the accumurate fitness of each individual
def pairwise_calculate_fitness(g,pm,w):
    payoff={}
    for d1 in g.nodes_iter():
        payoff[d1]=0
        for d2 in g.neighbors_iter(d1):
            mid1=np.dot([g.node[d1]['type'],1-g.node[d1]['type']],pm)
            payoff[d1]+=np.dot(mid1,[g.node[d2]['type'],1-g.node[d2]['type']])
        payoff[d1]=1-w+w*payoff[d1]
    nx.set_node_attributes(g,'fitness',payoff)
    return g

# select the individual for reproducation with a probability proportional to their fitness
def BD_selected_birth(g):
    nodes=g.nodes()
    totalfit=0
    for d1 in nodes:
        totalfit=totalfit+g.node[d1]['fitness']
    rand=rd.random()
    start=0
    end=g.node[nodes[0]]['fitness']/float(totalfit)
    for i in range(len(nodes)):
        if (rand>=start) and (rand<end):
            birth=nodes[i]    # birth is node
            break
        start=end
        end=end+g.node[nodes[i+1]]['fitness']/float(totalfit)
    return birth

# select the individual for reproduction in the death-birth process
def DB_selected_birth(g,death):
    totalfit=0
    for d1 in g.neighbors_iter(death):
        totalfit=totalfit+g.node[d1]['fitness']
    nodes=g.neighbors(death)
    rand=rd.random()
    start=0
    end=g.node[nodes[0]]['fitness']/float(totalfit)
    for i in range(len(nodes)):
        if (rand>=start) and (rand<end):
            birth=nodes[i]    # birth is node
            break
        start=end
        end=end+g.node[nodes[i+1]]['fitness']/float(totalfit)
    return birth

# simulate the evolutionary game with group BD updating
def group_BD_game_evol(g,game,w,nbunch,u,N):
    g=ed.add_dynamic_attributes(g,nbunch)
    result=[]
    i=0
    while i<N:
        g=group_calculate_fitness(g,game,w)
        birth=BD_selected_birth(g)
        death=ed.BD_random_death(g,birth)
        p=rd.random()
        if p>=u:
            g.node[death[0]]['type']=g.node[birth]['type']
        else:
            q=rd.random()
            if q>=0.5: g.node[death[0]]['type']=0
            else: g.node[death[0]]['type']=1
        cooper=ed.test_nodes_type(g)
        result.append(cooper)
        i+=1
    return result
        
# simulate the evolutionary game with pairwise BD updating
def pairwise_BD_game_evol(g,game,w,nbunch,u,N):
    g=ed.add_dynamic_attributes(g,nbunch)
    result=[]
    i=0
    while i<N:
        g=pairwise_calculate_fitness(g,game,w)
        birth=BD_selected_birth(g)
        death=ed.BD_random_death(g,birth)
        p=rd.random()
        if p>=u:
            g.node[death[0]]['type']=g.node[birth]['type']
        else:
            q=rd.random()
            if q>=0.5: g.node[death[0]]['type']=0
            else: g.node[death[0]]['type']=1
        cooper=ed.test_nodes_type(g)
        result.append(cooper)
        i+=1
    return result

# simulate the evolutionary game with group DB updating
def group_DB_game_evol(g,game,w,nbunch,u,N):
    g=ed.add_dynamic_attributes(g,nbunch)
    result=[]
    i=0
    while i<N:
        g=group_calculate_fitness(g,game,w)
        nodes=nx.nodes(g)
        death=rd.sample(nodes,1)
        birth=DB_selected_birth(g,death[0])
        p=rd.random()
        if p>=u:
            g.node[death[0]]['type']=g.node[birth]['type']
        else:
            q=rd.random()
            if q>=0.5: g.node[death[0]]['type']=0
            else: g.node[death[0]]['type']=1
        cooper=ed.test_nodes_type(g)
        result.append(cooper)
        i+=1
    return result

# simulate the evolutionary game with group DB updating
def pairwise_DB_game_evol(g,game,w,nbunch,u,N):
    g=ed.add_dynamic_attributes(g,nbunch)
    result=[]
    i=0
    while i<N:
        g=pairwise_calculate_fitness(g,game,w)
        nodes=nx.nodes(g)
        death=rd.sample(nodes,1)
        birth=DB_selected_birth(g,death[0])
        p=rd.random()
        if p>=u:
            g.node[death[0]]['type']=g.node[birth]['type']
        else:
            q=rd.random()
            if q>=0.5: g.node[death[0]]['type']=0
            else: g.node[death[0]]['type']=1
        cooper=ed.test_nodes_type(g)
        result.append(cooper)
        i+=1
    return result

# average cooperation level with cost-to-benefit ratio
def aver_coop_c(g,w,u,N):
    nodes=nx.nodes(g)
    s=g.order()
    nbunch=rd.sample(nodes,s/2)
    aver1=[]
    aver2=[]
    aver3=[]
    aver4=[]
    for c in range(11):
        c1=c/float(10)
        r_BD_grp=group_BD_game_evol(g,[[1,0],[1+c1,c1]],w,nbunch,u,N)
        r_BD_prw=pairwise_BD_game_evol(g,[[1,0],[1+c1,c1]],w,nbunch,u,N)
        r_DB_grp=group_DB_game_evol(g,[[1,0],[1+c1,c1]],w,nbunch,u,N)
        r_DB_prw=pairwise_DB_game_evol(g,[[1,0],[1+c1,c1]],w,nbunch,u,N)
        aver1.append(sum(r_BD_grp[N-2000:N])/len(r_BD_grp[N-2000:N]))
        aver2.append(sum(r_BD_prw[N-2000:N])/len(r_BD_prw[N-2000:N]))
        aver3.append(sum(r_DB_grp[N-2000:N])/len(r_DB_grp[N-2000:N]))
        aver4.append(sum(r_DB_prw[N-2000:N])/len(r_DB_prw[N-2000:N]))
    return (aver1,aver2,aver3,aver4)
    
def aver_times_c(g,w,u,N,M):
    aver=aver_coop_c(g,w,u,N)
    aver=np.array(aver)
    for i in range(M):
        aver1=np.array(aver_coop_c(g,w,u,N))
        aver=aver+aver1
    aver=aver/float(M+1)
    return aver

# simulate the evolutionary game to reach the fixation with group BD updating
def group_BD_game_fix(g,game,w,nbunch):
    g=ed.add_dynamic_attributes(g,nbunch)
    while True:
        g=group_calculate_fitness(g,game,w)
        birth=BD_selected_birth(g)
        death=ed.BD_random_death(g,birth)
        g.node[death[0]]['type']=g.node[birth]['type']
        cooper=ed.test_nodes_type(g)
        if cooper==0 or cooper==1: break
    return cooper

# do the simulation N times to approximately get the fixation probability
def group_BD_game_avfix(g,game,w,nbunch,N):
    fix=0
    for i in range(N):
        rslt=group_BD_game_fix(g,game,w,nbunch)
        fix+=rslt
        i+=1
    fix=float(fix)/N
    return fix

# find the average fixation probability for a random mutants
def group_BD_game_rdfix(g,game,w,N):
    aver=0
    for d in g.nodes_iter():
        fix=group_BD_game_avfix(g,game,w,[d],N)
        aver+=fix
    aver=float(aver)/g.order()
    return aver

# simulate the evolutionary game to reach the fixation with group DB updating
def group_DB_game_fix(g,game,w,nbunch):
    g=ed.add_dynamic_attributes(g,nbunch)
    while True:
        g=group_calculate_fitness(g,game,w)
        nodes=nx.nodes(g)
        death=rd.sample(nodes,1)
        birth=DB_selected_birth(g,death[0])
        g.node[death[0]]['type']=g.node[birth]['type']
        cooper=ed.test_nodes_type(g)
        if cooper==0 or cooper==1: break
    return cooper

# do the simulation N times to approximately get the fixation probability
def group_DB_game_avfix(g,game,w,nbunch,N):
    fix=0
    for i in range(N):
        rslt=group_DB_game_fix(g,game,w,nbunch)
        fix+=rslt
        i+=1
    fix=float(fix)/N
    return fix

# find the average fixation probability for a random mutants
def group_DB_game_rdfix(g,game,w,N):
    aver=0
    for d in g.nodes_iter():
        fix=group_DB_game_avfix(g,game,w,[d],N)
        aver+=fix
    aver=float(aver)/g.order()
    return aver

# calculate the structural coefficient of networks
def group_BD_stru_coef(g,w,N,M,c_int):
    rslt=[]
    c=[]
    fix_1=[]
    fix_2=[]
    for i in range(M):
        c1=c_int+0.02*i
        fix_a=group_BD_game_rdfix(g,[[1,0],[c1,0]],w,N)
        fix_b=group_BD_game_rdfix(g,[[0,c1],[0,1]],w,N)
        rslt.append(fix_a-fix_b)
        c.append(c1)
        fix_1.append(fix_a)
        fix_2.append(fix_b)
    return (rslt,c,fix_1,fix_2)

# simulate the evolutionary game to reach the fixation with pairwise BD updating
def pairwise_BD_game_fix(g,game,w,nbunch):
    g=ed.add_dynamic_attributes(g,nbunch)
    while True:
        g=pairwise_calculate_fitness(g,game,w)
        birth=BD_selected_birth(g)
        death=ed.BD_random_death(g,birth)
        g.node[death[0]]['type']=g.node[birth]['type']
        cooper=ed.test_nodes_type(g)
        if cooper==0 or cooper==1: break
    return cooper

# do the simulation N times to approximately get the fixation probability
def pairwise_BD_game_avfix(g,game,w,nbunch,N):
    fix=0
    for i in range(N):
        rslt=pairwise_BD_game_fix(g,game,w,nbunch)
        fix+=rslt
        i+=1
    fix=float(fix)/N
    return fix

# find the average fixation probability for a random mutants
def pairwise_BD_game_rdfix(g,game,w,N):
    aver=0
    for d in g.nodes_iter():
        fix=pairwise_BD_game_avfix(g,game,w,[d],N)
        aver+=fix
    aver=float(aver)/g.order()
    return aver    


# calculate the fixation probability for BD group interactions on complete networks
def group_BD_comp_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        prt=[]
        sum_rt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*(i+1)*(c-1))
            mid=mid*rt
            prt.append(mid)
            sum_rt+=mid
        rho_a=1.0/(1+sum_rt)
        rho_b=prt[N-2]/float(1+sum_rt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for DB group interactions on complete networks
def group_DB_comp_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        prt=[]
        sum_rt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*(i+1)*(c-1))*(i+1+(N-i-2)*np.exp(w*(i+1)*(c-1)))/float((i+(N-i-1)*np.exp(w*(i+1)*(c-1))))
            mid=mid*rt
            prt.append(mid)
            sum_rt+=mid
        rho_a=1.0/(1+sum_rt)
        rho_b=prt[N-2]/float(1+sum_rt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for BD pairwise interactions on complete networks
def pairwise_BD_comp_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        prt=[]
        sum_rt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*((i+1)*(c-1)+1))
            mid=mid*rt
            prt.append(mid)
            sum_rt+=mid
        rho_a=1.0/(1+sum_rt)
        rho_b=prt[N-2]/float(1+sum_rt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for DB pairwise interactions on complete networks
def pairwise_DB_comp_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        prt=[]
        sum_rt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*((i+1)*(c-1)+1))*(i+1+(N-i-2)*np.exp(w*((i+1)*(c-1)+1)))/float((i+(N-i-1)*np.exp(w*((i+1)*(c-1)+1))))
            mid=mid*rt
            prt.append(mid)
            sum_rt+=mid
        rho_a=1.0/(1+sum_rt)
        rho_b=prt[N-2]/float(1+sum_rt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for BD group interactions on cycle networks
def group_BD_cycl_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    p_a=[]
    p_a.append(1)
    p_a.append(5.0/3)
    for i in range(N-4):
        p_a.append(2)
    p_a.append(7.0/3)
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        p_b=[]
        p_b.append(2*c/3.0)
        for i in range(N-4):
            p_b.append(c)
        p_b.append(4*c/3.0)
        p_b.append(2*c)
        prt=[]
        srt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*(p_b[i]-p_a[i]))
            mid=mid*rt
            prt.append(mid)
            srt=srt+mid
        rho_a=1.0/(1+srt)
        rho_b=prt[N-2]/float(1+srt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for DB group interactions on cycle networks
def group_DB_cycl_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    p0_a=[]
    p0_a.append(1)
    p0_a.append(5.0/3)
    for i in range(N-4):
        p0_a.append(2)
    p0_a.append(7.0/3)
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        p0_b=[]
        p0_b.append(2*c/3.0)
        for i in range(N-4):
            p0_b.append(c)
        p0_b.append(4*c/3.0)
        p0_b.append(2*c)
        p1_a=[]
        p1_a.append(7/3.0)
        p1_b=[]
        for j in range(N-4):
            p1_a.append(8/3.0)
            p1_b.append(c/3.0)
        p1_b.append(2*c/3.0)
        prt=[]
        srt=0
        mid=1
        for i in range(N-1):
            if i==0:
                rt=(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(2*np.exp(w*p0_a[i]))
            elif i==1:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p0_a[i])+np.exp(w*p0_b[i])))
            elif i==N-3:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p0_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p1_a[i-2])+np.exp(w*p0_b[i])))
            elif i==N-2:
                rt=float(2*np.exp(w*p0_b[i]))/(np.exp(w*p0_b[i])+np.exp(w*p1_a[i-2]))
            else:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p1_a[i-2])+np.exp(w*p0_b[i])))   
            mid=mid*rt
            prt.append(mid)
            srt=srt+mid
        rho_a=1.0/(1+srt)
        rho_b=prt[N-2]/float(1+srt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for BD pairwise interactions on cycle networks
def pairwise_BD_cycl_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    p_a=[]
    p_a.append(0)
    for i in range(N-2):
        p_a.append(1)
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        p_b=[]
        for i in range(N-2):
            p_b.append(c)
        p_b.append(2*c)
        prt=[]
        srt=0
        mid=1
        for i in range(N-1):
            rt=np.exp(w*(p_b[i]-p_a[i]))
            mid=mid*rt
            prt.append(mid)
            srt=srt+mid
        rho_a=1.0/(1+srt)
        rho_b=prt[N-2]/float(1+srt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for DB pairwise interactions on cycle networks
def pairwise_DB_cycl_fix(w,N,M,c_int):
    rho_ac=[]
    rho_bc=[]
    c1=[]
    p0_a=[]
    p0_a.append(0)
    for i in range(N-2):
        p0_a.append(1)
    p1_a=[]
    p1_b=[]
    for i in range(N-3):
        p1_a.append(2)
        p1_b.append(0)
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        p0_b=[]
        for i in range(N-2):
            p0_b.append(c)
        p0_b.append(2*c)
        prt=[]
        srt=0
        mid=1
        for i in range(N-1):
            if i==0:
                rt=(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(2*np.exp(w*p0_a[i]))
            elif i==1:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p0_a[i])+np.exp(w*p0_b[i])))
            elif i==N-3:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p0_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p1_a[i-2])+np.exp(w*p0_b[i])))
            elif i==N-2:
                rt=float(2*np.exp(w*p0_b[i]))/(np.exp(w*p0_b[i])+np.exp(w*p1_a[i-2]))
            else:
                rt=np.exp(w*p0_b[i])*(np.exp(w*p1_b[i])+np.exp(w*p0_a[i]))/float(np.exp(w*p0_a[i])*(np.exp(w*p1_a[i-2])+np.exp(w*p0_b[i])))   
            mid=mid*rt
            prt.append(mid)
            srt=srt+mid
        rho_a=1.0/(1+srt)
        rho_b=prt[N-2]/float(1+srt)
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)
    
# calculate the fixation probability for BD group interactions on star networks
def group_BD_star_fix(w,N,M,c_int):
    ld_1=4*pow(N,4)-8*pow(N,3)+11*pow(N,2)-10*N+24
    ld_2=2*pow(N,4)+2*pow(N,3)-23*pow(N,2)+58*N-24
    ld_3=pow(N,4)+4*pow(N,3)-13*pow(N,2)+14*N+24
    ld_4=5*pow(N,4)-10*pow(N,3)+pow(N,2)+34*N-24
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        ma=1.0/(12*N)*(ld_1-ld_3*c)
        mb=1.0/(12*N)*(ld_2*c-ld_4)
        rho_a=1.0/N+w*pow((N-1),2)/(pow(N,2)*(pow(N,2)-2*N+2))*ma
        rho_b=1.0/N+w*pow((N-1),2)/(pow(N,2)*(pow(N,2)-2*N+2))*mb
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)
        
# calculate the fixation probability for DB group interactions on star networks
def group_DB_star_fix(w,N,M,c_int):
    ld_1=28*pow(N,2)-N-24
    ld_2=44*pow(N,2)-71*N+24
    ld_3=10*pow(N,2)+17*N-24
    ld_4=62*pow(N,2)-89*N+24
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        ma=1.0/(12*N)*(ld_1-ld_3*c)
        mb=1.0/(12*N)*(ld_2*c-ld_4)
        rho_a=1.0/N+w*(N-2)/(2*pow(N,2)*(N-1))*ma
        rho_b=1.0/N+w*(N-2)/(2*pow(N,2)*(N-1))*mb
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for BD pairwise interactions on star networks
def pairwise_BD_star_fix(w,N,M,c_int):
    ld_1=pow(N,3)-3*pow(N,2)+5*N-6
    ld_2=2*pow(N,3)-6*pow(N,2)+7*N+6
    ld_3=pow(N,3)-7*N+18
    ld_4=2*pow(N,3)-9*pow(N,2)+19*N-18
    Z=pow(N-1,2)/float(6*pow(N,2)*(pow(N,2)-2*N+2))
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        ma=Z*(ld_1-ld_3*c)
        mb=Z*(ld_2*c-ld_4)
        rho_a=1.0/N+w*ma
        rho_b=1.0/N+w*mb
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)

# calculate the fixation probability for DB pairwise interactions on star networks
def pairwise_DB_star_fix(w,N,M,c_int):
    Z=(N-2)/float(12*pow(N,3)*(N-2))
    ld_1=4*N-3
    ld_2=6*pow(N,2)-4*N-3
    rho_ac=[]
    rho_bc=[]
    c1=[]
    for i in range(M):
        c=c_int+0.01*i
        ma=Z*ld_1*(1-c)
        mb=Z*ld_2*(c-1)
        rho_a=1.0/N+w*ma
        rho_b=1.0/N+w*mb
        rho_ac.append(rho_a)
        rho_bc.append(rho_b)
        c1.append(c)
    return (rho_ac,rho_bc,c1)
    
        
        
        
