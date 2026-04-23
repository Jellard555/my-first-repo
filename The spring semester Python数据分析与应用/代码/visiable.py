import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5, 4), dpi=200)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
months = ["jan",'fre',"mar",'ari']
sales = [1,2,3,4]
goods = ['apple','banana','bear','grape']
color_line = "#9B7F25"
ax1.plot(months , sales, color = color_line, marker = "o")
ax2.bar(months , goods , color = "blue")
plt.show()
