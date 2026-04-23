import matplotlib.pyplot as plt
#设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = ['1953','1964','1982','1990','2000','2010','2020']
population = [58260,69458,100818,113368,126583,133972,141178]

plt.figure(figsize = (12,6))
bars = plt.bar(years,population,color = '#5c8cbc',edgecolor = 'black',linewidth = 1.5)
