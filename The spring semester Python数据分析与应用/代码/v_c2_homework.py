import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

month = ['Jan','Feb','Mar','Apr','May']
sales = [100,120,150,180,200]
improve_rate = [0.1,0.2,0.3,0.4,0.5]

fig,ax1 = plt.subplots(figsize = (10,6))

ax1.bar(month,sales,color = '#5c8cbc',linewidth = 1.5,label = "销售额")
ax1.set_xlabel('月份')
ax1.set_ylabel('销售额',color = "red")
ax1.tick_params(axis = 'y',labelcolor = "blue")

ax2 = ax1.twinx()
ax2.plot(month,improve_rate,color = 'yellow',linewidth = 1.5,label = "增长率")
ax2.set_ylabel('增长率',color = "green")
ax2.tick_params(axis = 'y',labelcolor = "blue")
lines1,labels1 = ax1.get_legend_handles_labels()
lines2,labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize = 10)

plt.tight_layout()
plt.show()
