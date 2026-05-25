import pandas as pd
import matplotlib.pyplot as plt
import re
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Zen Hei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
df = pd.read_csv("data.csv", encoding="utf-8-sig", header=None)
df.columns = ["大楼名称", "Standard height", "高度值1", "Total height", "高度值2", 
              "Floor count", "楼层数", "Observation decks", "观景台高度", 
              "Year built", "建成年份", "Uses", "用途", "Location", "城市"]
def extract_height(height_str):
    if pd.isna(height_str):
        return None
    match = re.search(r'(\d+\.?\d*)', str(height_str))
    return float(match.group(1)) if match else None

df['标准高度(米)'] = df['高度值1'].apply(extract_height)
top10 = df.dropna(subset=['标准高度(米)']).sort_values(by='标准高度(米)', ascending=False).head(20)
plt.figure(figsize=(10, 6))
bars = plt.barh(y=top10['大楼名称'][::-1],width=top10['标准高度(米)'][::-1],color="#34dbdb",edgecolor='white',height=0.7)
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5,bar.get_y() + bar.get_height()/2,f'{int(width)} m',va='center',fontsize=9)

plt.title('全球摩天大楼Top20标准高度排行', fontsize=14, pad=20, fontweight='bold')
plt.xlabel('标准高度（米）', fontsize=11)
plt.ylabel('大楼名称', fontsize=11)
plt.xlim(0, top10['标准高度(米)'].max() + 50)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()