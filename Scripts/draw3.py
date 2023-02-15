import bi_graph as bg
import matplotlib.pyplot as plt
import numpy as np

DB_heat=np.load('DB_bi_graph_heat.npy')
DB_deg=np.load('DB_bi_graph_deg.npy')
DB_09=np.load('DB_bi_graph_fix09.npy')
DB_11=np.load('DB_bi_graph_fix11.npy')

plt.figure(figsize=(3.43,2.57))

ax1=plt.subplot(411)
plt.plot(DB_heat,'ms')
plt.ylabel(r'$H_t(G)$',fontweight='heavy',fontsize=13)
plt.text(23,40,'(a)',fontweight='heavy',fontsize=13)

ax2=plt.subplot(412)
plt.plot(DB_09,'c<')
plt.ylabel(r'$\rho_1(0.9)$',fontweight='heavy',fontsize=13)
plt.text(23,0.015,'(b)',fontweight='heavy',fontsize=13)

ax3=plt.subplot(413)
plt.plot(DB_11,'g>')
plt.ylabel(r'$\rho_1(1.1)$',fontweight='heavy',fontsize=13)
plt.text(23,0.07,'(c)',fontweight='heavy',fontsize=13)

ax4=plt.subplot(414)
plt.plot(DB_deg,'ko')
plt.ylabel(r'$H_d(G)$',fontweight='heavy',fontsize=13)
plt.text(23,130,'(d)',fontweight='heavy',fontsize=13)

plt.xlabel(r'The number of nodes in set $U$',fontweight='heavy',fontsize=13)

plt.show()
