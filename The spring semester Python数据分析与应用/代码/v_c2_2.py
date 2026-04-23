import matplotlib.pyplot as plt
import numpy as np  
#数据准备
time = [0.00,0.05,0.50,0.75,1.00,1.25,1.50,1.75,2.00]
s1_s2_blue = [1.8,-1.5,2.5,-1.0,1.5,-1.5,1.0,-1.0,1.5]
s1_s2_orange = [0.5,0.2,0.9,0.1,0.2,0.1,0.2,0.1,0.2]
#创建图形和坐标轴
fig,ax = plt.subplots(figsize=(12,6),dpi = 200)
#绘制两条线
ax.plot(time,s1_s2_blue,color = 'blue',marker = 'o', linewidth = 9,markersize = 8,
        label = 's1_s2_blue(Blue)',markerfacecolor = 'blue',markeredgewidth = 2)
ax.plot(time,s1_s2_orange,color = 'orange',marker = 'o', linewidth = 2,markersize = 8,
        label = 's1_s2_orange(Orange)',markerfacecolor = 'orange',markeredgewidth = 2)

#添加水平线y=0
ax.axhline(y=0,color = 'black',linewidth = 1,linestyle = '--',alpha = 0.5)

#设置标题和坐标轴标签
ax.set_title('S1 and S2 Signals Over Time',fontsize = 14,fontweight = 'bold')
ax.set_xlabel('Time (s)',fontsize = 12)
ax.set_ylabel('Signal Amplitude',fontsize = 12)
ax.legend(fontsize = 12)

#设置x轴刻度
ax.set_xticks(time)
ax.set_xticklabels([f"{t:.2f}" for t in time],rotation = 60)

#设置y轴范围
ax.set_ylim(-2.,3.)
ax.legend(loc = 'upper right', fontsize = 10)
#添加网格
ax.grid(True,linestyle = '--',alpha = 0.5)

#调整布局
plt.tight_layout()
plt.show()
