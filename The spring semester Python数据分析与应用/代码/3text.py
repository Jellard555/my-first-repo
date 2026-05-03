from pyecharts.globals import CurrentConfig, OnlineHostType
# 切换为国内CDN
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/"

import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Map
from pyecharts.charts import Pie
from pyecharts import options as opts
import webbrowser
import os
import subprocess
df_school = pd.read_csv('university_rankings.csv',encoding="utf-8")
df_type_count = df_school.groupby("类型")  # 按“类型”分组
df_type_count = df_type_count.size()  # 统计每组数量
df_type_count = df_type_count.reset_index()  # 转成正常表格
df_type_count.columns = ["类型", "学校数量"]  # 重命名列名（完美匹配你的饼图）
print(df_type_count)


# 用pyecharts绘制饼图,也可以用matplotlib包

pie1 =(
Pie(init_opts=opts.InitOpts(theme='dark', bg_color='#0d0735')))# 设置主题和背景色
pie1.add(
"",
[list(z)for z in zip(df_type_count['类型'].tolist(), df_type_count['学校数量'].tolist())],
            radius=["40%","70%"],# 设置饼图为环状饼图
            label_opts=opts.LabelOpts(
                is_show=True,
                position="outside",# 标签位置
                formatter="{b}: {d}%",# 显示百分比
                font_size=12,# 标签字体大小
)
)
pie1.set_colors(['#e94e77','#f4a261','#2a9d8f','#264653','#e9c46a'])# 定义饼图颜色
pie1.set_global_opts(
            title_opts=opts.TitleOpts(
                title='2026中国大学各类型占比',
                pos_top='1%',
                pos_left="1%",
),
)
pie1.render()
file_path = os.path.abspath("render.html")
print(f"succeed!")
os.startfile(file_path)
