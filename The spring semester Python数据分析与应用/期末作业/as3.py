import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv("data.csv", encoding="utf-8-sig", header=None)
# 大楼名称、城市、年份、高度
building_data = []
for index, row in df.iterrows():
    tower_name = str(row.iloc[0]).strip()
    city = "未知"
    year = None
    height = None

    for i in range(1, len(row), 2):
        if i+1 >= len(row): break
        field = str(row.iloc[i]).strip()
        val = str(row.iloc[i+1]).strip()
        if "Location" in field:
            city = val
        if "Year built" in field:
            year = val
        if "Standard height" in field:
            height = val

    building_data.append({"大楼名称": tower_name,"城市": city,"建成年份": year,"标准高度": height})

df_new = pd.DataFrame(building_data)
def get_num(s):
    if pd.isna(s): return None
    match = re.search(r"\d+", str(s))
    return float(match.group()) if match else None

df_new["年份"] = df_new["建成年份"].apply(get_num)
df_new["高度_m"] = df_new["标准高度"].apply(get_num)
df_clean = df_new.dropna(subset=["年份", "高度_m"])
year_count = df_clean["年份"].value_counts().sort_index()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))  

ax1.plot(year_count.index, year_count.values, color="#ff7f0e", marker="o", linewidth=2, markersize=6)
ax1.set_title("年度建成数量趋势", fontsize=14, fontweight="bold")
ax1.set_xlabel("建成年份")
ax1.set_ylabel("建成数量")
ax1.grid(alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.scatter(df_clean["年份"], df_clean["高度_m"], c="#FF5733", s=80, alpha=0.8, edgecolors="white")
for _, row in df_clean.iterrows():
    x = row["年份"]
    y = row["高度_m"]
    name = row["大楼名称"]
    ax2.annotate(f"{name}\n({int(x)})", 
                 xy=(x, y), 
                 xytext=(5, 5), 
                 textcoords="offset points", 
                 fontsize=8)
ax2.set_title("建成年份与高度", fontsize=14, fontweight="bold")
ax2.set_xlabel("建成年份")
ax2.set_ylabel("标高（米）")
ax2.grid(alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)


plt.tight_layout()
plt.show()