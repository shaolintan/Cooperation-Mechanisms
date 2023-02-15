import bi_graph as bg
import matplotlib.pyplot as plt
import numpy as np

BD_heat=np.load('BD_bi_graph_heat.npy')
BD_deg=np.load('BD_bi_graph_deg.npy')
BD_09=np.load('BD_bi_graph_fix09.npy')
BD_11=np.load('BD_bi_graph_fix11.npy')

ax1=plt.subplot(411)
plt.plot(BD_heat,'ms')
plt.ylabel(r'$H_t(G)$',fontweight='heavy',fontsize=13)
plt.text(23,40,'(a)',fontweight='heavy',fontsize=13)

ax2=plt.subplot(412)
plt.plot(BD_09,'c<')
plt.ylabel(r'$\rho_1(0.9)$',fontweight='heavy',fontsize=13)
plt.text(23,0.0001,'(b)',fontweight='heavy',fontsize=13)

ax3=plt.subplot(413)
plt.plot(BD_11,'g>')
plt.ylabel(r'$\rho_1(1.1)$',fontweight='heavy',fontsize=13)
plt.text(23,0.155,'(c)',fontweight='heavy',fontsize=13)

ax4=plt.subplot(414)
plt.plot(BD_deg,'ko')
plt.ylabel(r'$H_d(G)$',fontweight='heavy',fontsize=13)
plt.text(23,130,'(d)',fontweight='heavy',fontsize=13)

plt.xlabel(r'The number of nodes in set $U$',fontweight='heavy',fontsize=13)

plt.show()

