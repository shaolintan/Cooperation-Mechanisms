import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

plt.subplot(331)
g1=nx.complete_graph(7)
nx.draw_circular(g1,node_color='white')

plt.subplot(332)
g2=nx.cycle_graph(7)
nx.draw_circular(g2,node_color='white')

plt.subplot(333)
g3=nx.star_graph(6)
nx.draw(g3,node_color='white')

ax1=plt.subplot(334)
GI_BD_comp_A=np.load('GI_BD_comp_A.npy')
GI_BD_comp_B=np.load('GI_BD_comp_B.npy')
PI_BD_comp_A=np.load('PI_BD_comp_A.npy')
PI_BD_comp_B=np.load('PI_BD_comp_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(0.8+0.01*i)
    c2.append(0.5+0.01*i)
plt.plot(c1,GI_BD_comp_A,'wo')
plt.plot(c1,GI_BD_comp_B,'ko')
plt.plot(c2,PI_BD_comp_A,'w*')
plt.plot(c2,PI_BD_comp_B,'k*')
plt.grid()
ax1.set_ylim(0.137)
x1=[0.99,0.99]
y1=[0.137,GI_BD_comp_A[19]]
plt.plot(x1,y1,'k-')
x2=[1.01,1.01]
y2=[0.137,GI_BD_comp_B[21]]
plt.plot(x2,y2,'k-')
x3=[0.71,0.71]
y3=[0.137,PI_BD_comp_A[21]]
plt.plot(x3,y3,'k-')
x4=[0.72,0.72]
y4=[0.137,PI_BD_comp_B[22]]
plt.plot(x4,y4,'k-')


ax2=plt.subplot(335)
GI_BD_cycle_A=np.load('GI_BD_cycle_A.npy')
GI_BD_cycle_B=np.load('GI_BD_cycle_B.npy')
PI_BD_cycle_A=np.load('PI_BD_cycle_A.npy')
PI_BD_cycle_B=np.load('PI_BD_cycle_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(1.4+0.01*i)
    c2.append(0.5+0.01*i)
plt.plot(c1,GI_BD_cycle_A,'wo')
plt.plot(c1,GI_BD_cycle_B,'ko')
plt.plot(c2,PI_BD_cycle_A,'w*')
plt.plot(c2,PI_BD_cycle_B,'k*')
plt.grid()
ax2.set_ylim(0.1415)
x1=[1.57,1.57]
y1=[0.1415,GI_BD_cycle_A[17]]
plt.plot(x1,y1,'k-')
x2=[1.58,1.58]
y2=[0.1415,GI_BD_cycle_B[18]]
plt.plot(x2,y2,'k-')
x3=[0.71,0.71]
y3=[0.1415,PI_BD_cycle_A[21]]
plt.plot(x3,y3,'k-')
x4=[0.72,0.72]
y4=[0.1415,PI_BD_cycle_B[22]]
plt.plot(x4,y4,'k-')


ax3=plt.subplot(336)
GI_BD_star_A=np.load('GI_BD_star_A.npy')
GI_BD_star_B=np.load('GI_BD_star_B.npy')
PI_BD_star_A=np.load('PI_BD_star_A.npy')
PI_BD_star_B=np.load('PI_BD_star_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(1.8+0.01*i)
    c2.append(0.6+0.01*i)
plt.plot(c1,GI_BD_star_A,'wo')
plt.plot(c1,GI_BD_star_B,'ko')
plt.plot(c2,PI_BD_star_A,'w*')
plt.plot(c2,PI_BD_star_B,'k*')
plt.grid()
ax3.set_ylim(0.139)
x1=[2.02,2.02]
y1=[0.139,GI_BD_star_A[22]]
plt.plot(x1,y1,'k-')
x2=[2.03,2.03]
y2=[0.139,GI_BD_star_B[23]]
plt.plot(x2,y2,'k-')
x3=[0.77,0.77]
y3=[0.139,PI_BD_star_A[17]]
plt.plot(x3,y3,'k-')
x4=[0.78,0.78]
y4=[0.139,PI_BD_star_B[18]]
plt.plot(x4,y4,'k-')

ax4=plt.subplot(337)
GI_DB_comp_A=np.load('GI_DB_comp_A.npy')
GI_DB_comp_B=np.load('GI_DB_comp_B.npy')
PI_DB_comp_A=np.load('PI_DB_comp_A.npy')
PI_DB_comp_B=np.load('PI_DB_comp_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(0.8+0.01*i)
    c2.append(0.5+0.01*i)
plt.plot(c1,GI_DB_comp_A,'wo')
plt.plot(c1,GI_DB_comp_B,'ko')
plt.plot(c2,PI_DB_comp_A,'w*')
plt.plot(c2,PI_DB_comp_B,'k*')
plt.grid()
ax4.set_ylim(0.137)
x1=[0.99,0.99]
y1=[0.137,GI_DB_comp_A[19]]
plt.plot(x1,y1,'k-')
x2=[1.01,1.01]
y2=[0.137,GI_DB_comp_B[21]]
plt.plot(x2,y2,'k-')
x3=[0.71,0.71]
y3=[0.137,PI_DB_comp_A[21]]
plt.plot(x3,y3,'k-')
x4=[0.72,0.72]
y4=[0.137,PI_DB_comp_B[22]]
plt.plot(x4,y4,'k-')

ax5=plt.subplot(338)
GI_DB_cycle_A=np.load('GI_DB_cycle_A.npy')
GI_DB_cycle_B=np.load('GI_DB_cycle_B.npy')
PI_DB_cycle_A=np.load('PI_DB_cycle_A.npy')
PI_DB_cycle_B=np.load('PI_DB_cycle_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(2.0+0.01*i)
    c2.append(1.6+0.01*i)
plt.plot(c1,GI_DB_cycle_A,'wo')
plt.plot(c1,GI_DB_cycle_B,'ko')
plt.plot(c2,PI_DB_cycle_A,'w*')
plt.plot(c2,PI_DB_cycle_B,'k*')
plt.grid()
ax5.set_ylim(0.1426)
x1=[2.21,2.21]
y1=[0.1426,GI_DB_cycle_A[22]]
plt.plot(x1,y1,'k-')
x2=[2.22,2.22]
y2=[0.1426,GI_DB_cycle_B[23]]
plt.plot(x2,y2,'k-')
x3=[1.85,1.85]
y3=[0.1426,PI_DB_cycle_A[25]]
plt.plot(x3,y3,'k-')
x4=[1.86,1.86]
y4=[0.1426,PI_DB_cycle_B[26]]
plt.plot(x4,y4,'k-')

ax6=plt.subplot(339)
GI_DB_star_A=np.load('GI_DB_star_A.npy')
GI_DB_star_B=np.load('GI_DB_star_B.npy')
PI_DB_star_A=np.load('PI_DB_star_A.npy')
PI_DB_star_B=np.load('PI_DB_star_B.npy')
c1=[]
c2=[]
for i in range(40):
    c1.append(1.4+0.01*i)
    c2.append(0.8+0.01*i)
plt.plot(c1,GI_DB_star_A,'wo')
plt.plot(c1,GI_DB_star_B,'ko')
plt.plot(c2,PI_DB_star_A,'w*')
plt.plot(c2,PI_DB_star_B,'k*')
plt.grid()
ax6.set_ylim(0.1427)
x1=[1.66,1.66]
y1=[0.1427,GI_DB_star_A[26]]
plt.plot(x1,y1,'k-')
x2=[1.67,1.67]
y2=[0.1427,GI_DB_star_B[27]]
plt.plot(x2,y2,'k-')
x3=[0.99,0.99]
y3=[0.1427,PI_DB_star_A[19]]
plt.plot(x3,y3,'k-')
x4=[1.01,1.01]
y4=[0.1427,PI_DB_star_B[21]]
plt.plot(x4,y4,'k-')


plt.show()
