import networkx as nx
import consensus_evol as ce
import numpy as np
import matplotlib.pyplot as plt

dis=np.random.random(10)
g1=nx.complete_graph(10)
g2=nx.cycle_graph(10)
g3=nx.star_graph(9)
#g4=nx.connected_watts_strogatz_graph(10,2,0.2)
#g5=nx.barabasi_albert_graph(10,3)
aver=sum(dis)/float(10)

s11=[]
s21=[]
s31=[]
#s41=[]
#s51=[]
s12=[]
s22=[]
s32=[]
#s42=[]
#s52=[]
s=[]
v=[]
for i in range(21):
    u=0.5*i
    rslt11=ce.interven_imi_evol_1(g1,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    rslt21=ce.interven_imi_evol_1(g2,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    rslt31=ce.interven_imi_evol_1(g3,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    #rslt41=ce.interven_imi_evol_1(g4,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    #rslt51=ce.interven_imi_evol_1(g5,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    rslt12=ce.interven_imi_evol_2(g1,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    rslt22=ce.interven_imi_evol_2(g2,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    rslt32=ce.interven_imi_evol_2(g3,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    #rslt42=ce.interven_imi_evol_2(g4,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
   # rslt52=ce.interven_imi_evol_2(g5,[[0.9,-0.1],[1,0]],dis,0.1,100,u)
    s11.append(rslt11[1][99]/float(2*g1.size()))
    s21.append(rslt21[1][99]/float(2*g2.size()))
    s31.append(rslt31[1][99]/float(2*g3.size()))
    #s41.append(rslt41[1][99]/float(2*g4.size()))
    #s51.append(rslt51[1][99]/float(2*g5.size()))
    s12.append(rslt12[1][99]/float(2*g1.size()))
    s22.append(rslt22[1][99]/float(2*g2.size()))
    s32.append(rslt32[1][99]/float(2*g3.size()))
    #s42.append(rslt42[1][99]/float(2*g4.size()))
    #s52.append(rslt52[1][99]/float(2*g5.size()))
    v.append(u)
    s.append(aver)
np.save('comp_reward',s11)
np.save('cycle_reward',s21)
np.save('star_reward',s31)
#np.save('small_world_reward',s41)
#np.save('scale_free_reward',s51)
np.save('comp_punish',s12)
np.save('cycle_punish',s22)
np.save('star_punish',s32)
#np.save('small_world_reward',s42)
#np.save('scale_free_reward',s52)
np.save('init_aver',s)
np.save('reward',v)
plt.plot(v,s11,'ro-')
plt.plot(v,s21,'bo-')
plt.plot(v,s31,'mo-')
#plt.plot(v,s41,'co-')
#plt.plot(v,s51,'go-')
plt.plot(v,s12,'rs-')
plt.plot(v,s22,'bs-')
plt.plot(v,s32,'ms-')
#plt.plot(v,s42,'cs-')
#plt.plot(v,s52,'gs-')
plt.plot(v,s,'k--')
plt.xlabel(r'The rewards or punishment $u$',fontweight='heavy',fontsize=13)
plt.ylabel('The cooperation level',fontweight='heavy',fontsize=13)
plt.show()
