import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv("data.csv", encoding="utf-8-sig", header=None)
df.columns = ["大楼名称", "Standard height", "高度值1", "Total height", "高度值2",
              "Floor count", "楼层数", "Observation decks", "观景台高度",
              "Year built", "建成年份", "Uses", "用途", "Location", "城市"]

# 大楼名称 + 城市
building_data = []
for index, row in df.iterrows():
    tower_name = str(row.iloc[0]).strip()
    city = "未知城市"
    for i in range(1, len(row), 2):
        if i + 1 >= len(row):
            break
        field = str(row.iloc[i]).strip()
        value = str(row.iloc[i+1]).strip()
        if "Location" in field:
            city = value
            break    
    building_data.append({"大楼名称": tower_name, "城市": city})
new_df = pd.DataFrame(building_data)
#print(new_df)

city_to_country = {"Dubai": "阿联酋","Kuala Lumpur": "马来西亚","Shanghai": "中国","Mecca": "沙特阿拉伯","Shenzhen": "中国","Tianjin": "中国","Seoul": "韩国",
    "New York City": "美国","Guangzhou": "中国","Beijing": "中国","Taipei": "中国","Hong Kong": "中国","Wuhan": "中国","St. Petersburg": "俄罗斯","Ho Chi Minh City": "越南","Nanjing": "中国","Changsha": "中国","Melbourne": "澳大利亚","Chicago": "美国","Jakarta": "印尼","Bangkok": "泰国","Mumbai": "印度","Manila": "菲律宾","Toronto": "加拿大","Mexico City": "墨西哥"}
new_df["国家"] = new_df["城市"].map(city_to_country)
new_df["国家"] = new_df["国家"].fillna("其他")
country_count = new_df["国家"].value_counts()
print(country_count)

plt.figure(figsize=(20, 9))
ax1 = plt.subplot(1, 2, 1)
bars = plt.bar(country_count.index, country_count.values, color="#2E86AB")
for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 0.1, f"{int(h)}", ha="center")

ax1.set_title("20栋摩天大楼 国家分布柱状图", fontsize=14)
ax1.set_xlabel("国家")
ax1.set_ylabel("大楼数量")
ax1.set_ylim(0, max(country_count.values) + 1)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax2 = plt.subplot(1, 2, 2)
colors = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D", "#6A994E", "#7209B7", 
          "#F72585", "#4361EE", "#F77F00", "#FCBF49", "#E9ECEF"]  
explode = [0.05 if country == country_count.index[0] else 0 for country in country_count.index]

wedges, texts, autotexts = ax2.pie(country_count.values, labels=country_count.index, autopct="%1.1f%%",
    startangle=100,colors=colors[:len(country_count)],explode=explode,textprops={"fontsize": 10})
ax2.set_title("20栋摩天大楼 国家分布饼图", fontsize=14)
ax2.axis("equal")  # 保持饼图为圆形

plt.tight_layout()
plt.savefig("country_distribution.png", dpi=300)
plt.show()